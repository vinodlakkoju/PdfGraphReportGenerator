import numpy as np
import io
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
from PIL import Image


def radar_factory(num_vars, frame='circle'):
    """Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle' | 'polygon'}
        Shape of frame surrounding axes.

    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

    class RadarTransform(PolarAxes.PolarTransform):
        def transform_path_non_affine(self, path):
            # Paths with non-unit interpolation steps correspond to gridlines,
            # in which case we force interpolation (to defeat PolarTransform's
            # autoconversion to circular arcs).
            if path._interpolation_steps > 1:
                path = path.interpolated(num_vars)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):
        name = 'radar'
        PolarTransform = RadarTransform
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                pass
                # return RegularPolygon((0.5, 0.5), num_vars, radius=.5, edgecolor="k")
                return RegularPolygon((0.5, 0.5), num_vars, radius=.5)
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

        def draw(self, renderer):
            """ Draw. If frame is polygon, make gridlines polygon-shaped """
            if frame == 'polygon':
                gridlines = self.yaxis.get_gridlines()
                for gl in gridlines:
                    gl.get_path()._interpolation_steps = num_vars
            super().draw(renderer)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)

                return {'polar': spine}
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta


def drawSpiderPlot(data):
    spoke_labels = [' ' for item in data.keys()]
    case_data = data.values()
    theta = radar_factory(len(spoke_labels), frame='polygon')

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='radar'))
    ax.set_rgrids([item for item in range(0, 100, 10)], angle=270)

    line = ax.plot(theta, case_data)
    # ax.fill(theta, case_data, alpha=0.25, label='_nolegend_')
    ax.set_varlabels(spoke_labels)
    #plt.show()
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')

    im = Image.open(img_buf)
    im.show(title="My Image")

    img_buf.close()




if __name__ == '__main__':
    behaviour_data = {
        'Hero': 40,
        'Achiever': 80,
        'Engineer': 70,
        'Protector': 90,
        'Angel': 60,
        'Creator': 60,
        'Discoverer': 50,
        'Influencer': 70,
        'Strategist': 50
    }
    competency_data = {
        'strategic_thinking': 40,
        'team_work': 90,
        'purpose_driven': 70,
        'process_oriented': 30,
        'communications': 80,
        'leader_ship': 40,
        'problem_solving': 90,
        'customer_focus': 30,
        'creativity': 90,
        'service_oriented': 40,
        'decision_making': 90,
        'planning': 60,
    }
    competency_data1 = {
        'strategic_thinking': 40,
        'team_work': 40,
        'purpose_driven': 40,
        'process_oriented': 40,
        'communications': 40,
        'leader_ship': 40,
        'problem_solving': 40,
        'customer_focus': 40,
        'creativity': 40,
        'service_oriented': 40,
        'decision_making': 40,
        'planning': 40,
    }
    drawSpiderPlot(competency_data)
