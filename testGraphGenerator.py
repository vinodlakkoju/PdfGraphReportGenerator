import unittest
from ReportsService.GraphGenerator import GraphGenerator
from ReportsService.Constants import GraphType
import sys
sys.path.insert(0, r'../Images')


class TestGraphGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.graph_obj = GraphGenerator()
        self.behaviour_data = {
            'role': {
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
            'candidate': {
                "Hero": "60",
                "Strategist": "70",
                "Influencer": "80",
                "Discoverer": "20",
                "Creator": "40",
                "Angel": "30",
                "Protector": "70",
                "Engineer": "80",
                "Achiever": "20"
            }
        }
        self.competency_data = {'role': {
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
        self.values_data = {
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

    def testGenerateGraphBehaviour(self):
        b_graph = self.graph_obj.generateGraph(graph_type=GraphType.behaviour_benchmark,
                                               benchmark=self.behaviour_data)
        b_graph.show()
        self.assertIsNotNone(b_graph, "Test-1 failed")

    def testGenerateGraphCompetency(self):
        c_graph = self.graph_obj.generateGraph(graph_type=GraphType.competency_benchmark,
                                               benchmark=self.competency_data)
        self.assertIsNotNone(c_graph, "Test-2 failed")

    def testGenerateGraphValues(self):
        v_graph = self.graph_obj.generateGraph(graph_type=GraphType.values_benchmark, benchmark=self.values_data)
        self.assertIsNotNone(v_graph, "Test-3 failed")


if __name__ == '__main__':
    unittest.main()
