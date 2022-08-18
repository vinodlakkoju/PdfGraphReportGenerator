import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
from typing import Dict
import Constants as cons
from SpiderGraph import radar_factory


class GraphGenerator:
    """
    This class creates graph images
    """
    def __init__(self):
        pass

    @staticmethod
    def __fillTrasperant(img):
        """
        This method replaces all white pixels transparent pixels on the input image
        :param img: image with white background
        :return: image with transparent background
        """
        img = img.convert("RGBA")
        imgnp = np.array(img)

        white = np.sum(imgnp[:, :, :3], axis=2)
        white_mask = np.where(white == 255 * 3, 1, 0)

        alpha = np.where(white_mask, 0, imgnp[:, :, -1])
        imgnp[:, :, -1] = alpha
        img = Image.fromarray(np.uint8(imgnp))
        return img

    @staticmethod
    def __addMargin(pil_img, top, right, bottom, left, color):
        """
        This method adjust the boundaries of the image with provided input values
        :param pil_img: Image to be adjusted
        :param top: Top limit of the image
        :param right: Right limit of the image
        :param bottom: Bottom limit of the image
        :param left: Left limit of the image
        :param color: Color of the adjusted pixels on the image
        :return: Image with adjusted limits
        """
        width, height = pil_img.size
        new_width = width + right + left
        new_height = height + top + bottom
        result = Image.new(pil_img.mode, (new_width, new_height), color)
        result.paste(pil_img, (left, top))
        return result

    def generateGraph(self, graph_type: cons.GraphType, benchmark: Dict) -> Image:
        """
        This method generates a graph
        :param graph_type: Behaviour or Competency
        :param benchmark: Benchmark values
        :return: A graph image with given input params
        """
        if not benchmark:
            raise ValueError('No data to plot graph')
        try:
            element_count = 0
            if graph_type.value == cons.GraphType.behaviour_benchmark.value:
                image = cons.BEHAVIOUR_MATCHING_BG_IMAGE if 'role' in benchmark and 'candidate' in benchmark else cons.BEHAVIOUR_BG_IMAGE
                element_count = cons.BEHAVIOUR_GRAPH_ELEMENT_COUNT
            elif graph_type.value == cons.GraphType.competency_benchmark.value:
                image = cons.COMPETENCY_MATCHING_BG_IMAGE if 'role' in benchmark and 'candidate' in benchmark else cons.COMPETENCY_BG_IMAGE
                element_count = cons.COMPETENCY_GRAPH_ELEMENT_COUNT
            elif graph_type.value == cons.GraphType.values_benchmark.value:
                element_count = cons.VALUE_GRAPH_ELEMENT_COUNT

            if not element_count:
                raise Exception('Invalid Data to generate graph')
            role_data_points = []
            candidate_data_points = []
            spoke_labels = []
            if 'role' in benchmark:
                data = dict(list(benchmark['role'].items())[:element_count])
                role_data_points = [int(value) for value in data.values()]
                spoke_labels = [item for item in data.keys()] if graph_type == cons.GraphType.values_benchmark else [' ' for item in data.keys()]
            if 'candidate' in benchmark:
                data = dict(list(benchmark['candidate'].items())[:element_count])
                candidate_data_points = [int(value) for value in data.values()]
                spoke_labels = [item for item in data.keys()] if graph_type == cons.GraphType.values_benchmark else [' ' for item in data.keys()]

            theta = radar_factory(len(spoke_labels), frame='polygon')
            fig, ax = plt.subplots(figsize=(7.5, 7.5), subplot_kw=dict(projection='radar'))
            ax.set_rgrids([item for item in range(0, 100, 10)], angle=0)
            if role_data_points:
                line = ax.plot(theta, role_data_points)
                ax.fill(theta, role_data_points, alpha=0.25)
            if candidate_data_points:
                line = ax.plot(theta, candidate_data_points)
                ax.fill(theta, candidate_data_points, alpha=0.25)
            ax.set_varlabels(spoke_labels)
            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')

            img_fg = Image.open(img_buf)
            img_fg = self.__addMargin(img_fg, 125, 125, 125, 125, (255, 255, 255))
            if graph_type == cons.GraphType.values_benchmark:
                final_image = Image.new("RGBA", img_fg.size)
                final_image = Image.alpha_composite(final_image, self.__fillTrasperant(img_fg))
                return final_image
            else:
                img_bg = Image.open(image)
                img_bg = img_bg.resize((cons.BG_IMAGE_SIZE, cons.BG_IMAGE_SIZE), Image.ANTIALIAS)
                final_image = Image.new("RGBA", img_bg.size)
                final_image = Image.alpha_composite(final_image, img_bg)
                final_image = Image.alpha_composite(final_image, self.__fillTrasperant(img_fg))
                print('Created graph images')
                return final_image
        except Exception as ex:
            print(f"Error : {ex}")


def main():
    behaviour_data = {'role': {
        "Hero": "30",
        "Strategist": "40",
        "Influencer": "50",
        "Discoverer": "30",
        "Creator": "20",
        "Angel": "70",
        "Protector": "60",
        "Engineer": "50",
        "Achiever": "40"
    },
    #     'candidate': {
    #     "Hero": "60",
    #     "Strategist": "70",
    #     "Influencer": "80",
    #     "Discoverer": "20",
    #     "Creator": "40",
    #     "Angel": "30",
    #     "Protector": "70",
    #     "Engineer": "80",
    #     "Achiever": "20"
    # }
    }
    competency_data = {'role': {
        "strategic_thinking": "40",
        "team_work": "90",
        "purpose_driven": "70",
        "process_oriented": "30",
        "communications": "80",
        "leader_ship": "40",
        "problem_solving": "90",
        "customer_focus": "30",
        "creativity": "90",
        "service_oriented": "40",
        "decision_making": "90",
        "planning": "60"
    }}
    values_data = {
        'Inclusive': {
            'role': {
                'Harmonising': '20',
                'Flattering': '30',
                'Sympathetic': '25',
                'Encouraging': '60',
                'Purposeful': '50'
            },
            'candidate': {
                'Harmonising': '30',
                'Flattering': '40',
                'Sympathetic': '35',
                'Encouraging': '70',
                'Purposeful': '60'
            }
        }
    }
    img_obj = GraphGenerator()
    # b_graph = img_obj.generateGraph(graph_type=cons.GraphType.behaviour_benchmark, benchmark=behaviour_data)
    # b_graph.show()
    c_graph = img_obj.generateGraph(graph_type=cons.GraphType.competency_benchmark, benchmark=competency_data)
    c_graph.show()
    #v_graph = img_obj.generateGraph(graph_type=cons.GraphType.values_benchmark, benchmark=values_data['Inclusive'])
    #v_graph.show()


if __name__ == '__main__':
    main()
