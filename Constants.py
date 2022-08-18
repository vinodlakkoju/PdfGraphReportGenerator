from enum import Enum, auto


class BuildType(Enum):
    build_local = auto(),
    build_dev = auto(),
    build_prod = auto()

class GraphType(Enum):
    behaviour_benchmark = auto()
    competency_benchmark = auto()
    values_benchmark = auto()
    vacancy_report = auto()
    candidate_report = auto()


CELL_HEIGHT = 7
PAGE_WIDTH = 190
BG_IMAGE_SIZE = 1000
FG_IMAGE_SIZE = 750
BEHAVIOUR_GRAPH_ELEMENT_COUNT = 9
COMPETENCY_GRAPH_ELEMENT_COUNT = 12
VALUE_GRAPH_ELEMENT_COUNT = 5
BEHAVIOUR_BG_IMAGE = r"Images_v2/vacancy-behaviour-bg.png"
COMPETENCY_BG_IMAGE = r"Images_v2/vacancy-competency-bg.png"
BEHAVIOUR_MATCHING_BG_IMAGE = r"Images_v2/behaviour_matching.png"
COMPETENCY_MATCHING_BG_IMAGE = r"Images_v2/competency_matching.png"

MATCHING_PDF_FIRST_PAGE_IMAGE = r'./Images_v2/matching_pdf_first_page.png'
VACANCY_PDF_FIRST_PAGE_IMAGE = r'./Images_v2/vacancy_pdf_first_page.png'
VACANCY_ROLL_DETAILS_PAGE_IMAGE = r'./Images_v2/roll-details-page.png'
VACANCY_RESPONSIBILITIES_PAGE_IMAGE = r'./Images_v2/responsibilities-page.png'
VACANCY_SKILLS_PAGE_IMAGE = r'./Images_v2/skills-page.png'
VACANCY_BEHAVIOUR_PAGE_IMAGE = r'./Images_v2/behaviour-benchmark-page.png'
VACANCY_COMPETENCY_PAGE_IMAGE = r'./Images_v2/competency-benchmark-page.png'

PDF_MID_PAGE_IMAGE = r'./Images_v2/pdf_mid_page.png'
PDF_LAST_PAGE_IMAGE = r'./Images_v2/pdf_last_page.png'

BUILD_TYPE = BuildType.build_local
if BUILD_TYPE == BuildType.build_dev:
    TEMP_IMAGE_FILE_PATH = r'/uploads'
    REST_API_URL = 'https://dev.services.compaira.com:8080'
elif BUILD_TYPE == BuildType.build_prod:
    TEMP_IMAGE_FILE_PATH = r'/uploads'
    REST_API_URL = 'https://services.compaira.com:8080'
else:
    TEMP_IMAGE_FILE_PATH = r'c:\temp'
    REST_API_URL = 'http://localhost:8080'

REST_API_VACANCY_DATA_URL = f'{REST_API_URL}/reports/vacancydata'
REST_API_MATCHING_DATA_URL = f'{REST_API_URL}/reports/matchingdata'
REST_API_BEHAVIOUR_DATA_URL = f'{REST_API_URL}/reports/behaviourdata'
REST_API_COMPETENCY_DATA_URL = f'{REST_API_URL}/reports/competencydata'
REST_API_VALUES_DATA_URL = f'{REST_API_URL}/reports/valuesdata'

EMPTY_BEHAVIOUR_BENCHMARK = {"Hero": "0", "Achiever": "0", "Engineer": "0", "Protector": "0", "Angel": "0",
                             "Creator": "0", "Discoverer": "0", "Influencer": "0", "Strategist": "0"}
EMPTY_COMPETENCY_BENCHMARK = {"strategic_thinking": "0", "team_work": "0", "purpose_driven": "0",
                              "process_oriented": "0", "communications": "0", "leader_ship": "0",
                              "problem_solving": "0", "customer_focus": "0","creativity": "0", "service_oriented": "0",
                              "decision_making": "0", "planning": "0"}

null = ''
