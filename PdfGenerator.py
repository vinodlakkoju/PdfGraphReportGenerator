import json
import os
from time import time
import pandas as pd
from fpdf import FPDF
from PIL import Image
from typing import Dict
import Constants as cons
from Utils import Utils as ut
from GraphGenerator import GraphGenerator


class PdfGenerator:
    """
    This class generates PDF report
    """
    def __init__(self, report_data: Dict) -> None:
        """
        Constructor to initialise pdf parameters
        :param report_data: Input data to generate PDF report
        """
        self.__pdf = FPDF()
        self.__report_data = report_data
        self.__effective_page_width = self.__pdf.w - 2 * self.__pdf.l_margin
        self.__graph = GraphGenerator()

    def __addImagePage(self, image_file: str) -> None:
        """
        This method creates a pdf page with image
        :param image_file: input image file to plot on pdf page
        :return: None
        """
        cover = Image.open(image_file)
        width, height = cover.size
        width, height = float(width * 0.15), float(height * 0.15)
        self.__pdf.add_page()
        self.__pdf.image(image_file, x=0, y=0, w=width, h=height)

    def __addRoleDetailsPage(self) -> None:
        image_file = cons.VACANCY_ROLL_DETAILS_PAGE_IMAGE
        cover = Image.open(image_file)
        width, height = cover.size
        width, height = float(width * 0.085), float(height * 0.085)
        self.__pdf.add_page()
        self.__pdf.image(image_file, x=0, y=0, w=width, h=height)
        # Role
        self.__pdf.set_xy(65, 30)
        self.__pdf.set_font('Arial', 'B', 20)
        self.__pdf.cell(80, 10, f'{ut.cleanText(self.__report_data["role"])}', 0, 2, 'C')
        # Description
        self.__pdf.set_xy(22, 75)
        self.__pdf.set_font('Arial', 'B', 10)
        self.__pdf.multi_cell(170, 5, f'{ut.cleanText(self.__report_data["description"])}')
        # Other Details
        other_data = self.__report_data["role_details"]
        sector = other_data["job_sector"]
        if sector:
            self.__pdf.set_xy(60, 130)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, sector.replace('_', ' '), 0, 2, 'L')
        area = other_data["functional_area"]
        if area:
            self.__pdf.set_xy(60, 140)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, area.capitalize(), 0, 2, 'L')
        level = other_data["job_level"]
        if level:
            self.__pdf.set_xy(60, 150)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, level.capitalize(), 0, 2, 'L')
        location = other_data["vacancy_location"]
        if location:
            self.__pdf.set_xy(60, 160)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, location.capitalize(), 0, 2, 'L')
        experience = other_data["preferred_experience"]
        if experience:
            self.__pdf.set_xy(60, 170)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(experience), 0, 2, 'L')
        tests = other_data["aptitude_test"]
        if tests:
            self.__pdf.set_xy(60, 180)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(tests), 0, 2, 'L')
        behaviour_variance = other_data["behaviour_variance"]
        if behaviour_variance:
            self.__pdf.set_xy(25, 213)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(behaviour_variance), 0, 2, 'L')
        competence_variance = other_data["competence_variance"]
        if competence_variance:
            self.__pdf.set_xy(55, 213)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(competence_variance), 0, 2, 'L')
        values_variance = other_data["values_variance"]
        if values_variance:
            self.__pdf.set_xy(85, 213)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(values_variance), 0, 2, 'L')
        weightage_cv = other_data["weightage_cv"]
        if weightage_cv:
            self.__pdf.set_xy(26, 258)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(weightage_cv), 0, 2, 'L')
        weightage_functionalSkills = other_data["weightage_functionalSkills"]
        if weightage_functionalSkills:
            self.__pdf.set_xy(56, 258)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(weightage_functionalSkills), 0, 2, 'L')
        weightage_technicalSkills = other_data["weightage_technicalSkills"]
        if weightage_technicalSkills:
            self.__pdf.set_xy(86, 258)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(weightage_technicalSkills), 0, 2, 'L')
        weightage_behaviour = other_data["weightage_behaviour"]
        if weightage_behaviour:
            self.__pdf.set_xy(117, 258)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(weightage_behaviour), 0, 2, 'L')
        weightage_competency = other_data["weightage_competency"]
        if weightage_competency:
            self.__pdf.set_xy(147, 258)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(weightage_competency), 0, 2, 'L')
        weightage_values = other_data["weightage_values"]
        if weightage_values:
            self.__pdf.set_xy(177, 258)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(50, 10, str(weightage_values), 0, 2, 'L')

    def __addResponsibiliesPage(self):
        image_file = cons.VACANCY_RESPONSIBILITIES_PAGE_IMAGE
        cover = Image.open(image_file)
        width, height = cover.size
        width, height = float(width * 0.085), float(height * 0.085)
        self.__pdf.add_page()
        self.__pdf.image(image_file, x=0, y=0, w=width, h=height)
        # Role
        self.__pdf.set_xy(65, 30)
        self.__pdf.set_font('Arial', 'B', 20)
        self.__pdf.cell(80, 10, f'{ut.cleanText(self.__report_data["role"])}', 0, 2, 'C')
        # Responsibilities
        self.__pdf.set_xy(22, 75)
        self.__pdf.set_font('Arial', 'B', 10)
        self.__pdf.multi_cell(170, 5, f'{ut.cleanText(self.__report_data["responsibilities"])}')

    def __addSkillsPage(self):
        image_file = cons.VACANCY_SKILLS_PAGE_IMAGE
        cover = Image.open(image_file)
        width, height = cover.size
        width, height = float(width * 0.085), float(height * 0.085)
        self.__pdf.add_page()
        self.__pdf.image(image_file, x=0, y=0, w=width, h=height)
        # Functional Skills
        self.__pdf.set_xy(22, 45)
        self.__pdf.set_font('Arial', 'B', 10)
        self.__pdf.multi_cell(170, 5, f'{ut.cleanText(self.__report_data["functional_skills"])}')
        # Technical Skills
        self.__pdf.set_xy(22, 165)
        self.__pdf.set_font('Arial', 'B', 10)
        self.__pdf.multi_cell(170, 5, f'{ut.cleanText(self.__report_data["technical_skills"])}')

    def __addBehaviourBenchmarkPage(self):
        image_file = cons.VACANCY_BEHAVIOUR_PAGE_IMAGE
        cover = Image.open(image_file)
        width, height = cover.size
        width, height = float(width * 0.085), float(height * 0.085)
        self.__pdf.add_page()
        self.__pdf.image(image_file, x=0, y=0, w=width, h=height)
        data = self.__report_data['behaviour_benchmark']
        # Add values
        self.__pdf.set_font('Arial', 'B', 10)
        x_position = 40
        y_position = 22
        for key, value in data['role'].items():
            self.__pdf.set_xy(x_position, y_position)
            self.__pdf.cell(10, 50, key, 0, 2, 'L')
            self.__pdf.set_xy(x_position + 105, y_position)
            self.__pdf.cell(10, 50, str(value), 0, 2, 'L')
            y_position += 7.6

        # Add Graph Image
        graph_type = cons.GraphType.behaviour_benchmark
        graph_image = self.__graph.generateGraph(graph_type=graph_type, benchmark=data)
        file_name = f'image_behaviour_{self.__report_data["role_id"]}_{str(time()).replace(".", "")}.png'
        file_path = os.path.join(cons.TEMP_IMAGE_FILE_PATH, file_name)
        graph_image.save(file_path, 'png')
        # Draw Benchmark image
        width, height = graph_image.size
        width, height = float(width * 0.15), float(height * 0.15)
        self.__pdf.image(file_path, x=20, y=112, w=width, h=height)

    def __addCompetencyBenchmarkPage(self):
        image_file = cons.VACANCY_COMPETENCY_PAGE_IMAGE
        cover = Image.open(image_file)
        width, height = cover.size
        width, height = float(width * 0.085), float(height * 0.085)
        self.__pdf.add_page()
        self.__pdf.image(image_file, x=0, y=0, w=width, h=height)
        data = self.__report_data['competency_benchmark']
        # Add values
        self.__pdf.set_font('Arial', 'B', 10)
        x_position = 40
        y_position = 22
        for key, value in data['role'].items():
            self.__pdf.set_xy(x_position, y_position)
            self.__pdf.cell(10, 50, key.replace('_', ' ').capitalize(), 0, 2, 'L')
            self.__pdf.set_xy(x_position + 105, y_position)
            self.__pdf.cell(10, 50, str(value), 0, 2, 'L')
            y_position += 7.6
        # Add Graph Image
        graph_type = cons.GraphType.competency_benchmark
        graph_image = self.__graph.generateGraph(graph_type=graph_type, benchmark=data)
        file_name = f'image_competency_{self.__report_data["role_id"]}_{str(time()).replace(".", "")}.png'
        file_path = os.path.join(cons.TEMP_IMAGE_FILE_PATH, file_name)
        graph_image.save(file_path, 'png')
        # Draw Benchmark image
        width, height = graph_image.size
        width, height = float(width * 0.15), float(height * 0.15)
        self.__pdf.image(file_path, x=20, y=135, w=width, h=height)

    def __addTextPage(self, content: str = None) -> None:
        image_file = cons.PDF_MID_PAGE_IMAGE
        cover = Image.open(image_file)
        width, height = cover.size
        width, height = float(width * 0.15), float(height * 0.15)
        self.__pdf.add_page()
        self.__pdf.image(image_file, x=0, y=0, w=width, h=height)
        self.__pdf.set_xy(0, 0)

        if content == 'role':
            self.__pdf.set_font('Arial', 'B', 20)
            self.__pdf.cell(200, 270, f'{content.replace("_", " ").capitalize()}: {ut.cleanText(self.__report_data["role"])}', 0, 2, 'C')
        else:
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.ln(30)
            self.__pdf.cell(w=1, h=0, txt=f'{content.replace("_", " ").capitalize()}:', border=0, ln=1, align='L')
            self.__pdf.ln(10)
            self.__pdf.set_font('Arial', '', 13)
            if content == 'role_details':
                data = self.__report_data[content]
                for key, value in data.items():
                    self.__pdf.cell(w=1, h=0, txt=f'{key.replace("_", " ").capitalize()}: {value}', border=0, ln=1, align='L')
                    self.__pdf.ln(7)
            elif content == 'responsibilities':
                # for item in self.__report_data[content].replace('\n', '').split('.'):
                #    self.__pdf.multi_cell(self.__effective_page_width, 7, f'  * {ut.cleanText(item)}')
                data = ut.cleanText(self.__report_data[content])
                self.__pdf.multi_cell(self.__effective_page_width, 7, data)
            # elif content in ['functional_skills', 'technical_skills']:
            #     data = ut.cleanText(self.__report_data[content])
            #     self.__pdf.multi_cell(self.__effective_page_width, 7, data)
            elif content == 'skills':
                # Add Functional skills
                self.__pdf.set_font('Arial', 'B', 13)
                self.__pdf.ln(15)
                self.__pdf.cell(w=1, h=0, txt='Functional Skills:', border=0, ln=1, align='L')
                self.__pdf.ln(10)
                self.__pdf.set_font('Arial', '', 13)
                data = ut.cleanText(self.__report_data['functional_skills'])
                self.__pdf.multi_cell(self.__effective_page_width, 7, data)
                # Add Technical Skills
                self.__pdf.set_font('Arial', 'B', 13)
                self.__pdf.ln(10)
                self.__pdf.cell(w=1, h=0, txt=f'Technical Skills:', border=0, ln=1, align='L')
                self.__pdf.ln(10)
                self.__pdf.set_font('Arial', '', 13)
                data = ut.cleanText(self.__report_data['technical_skills'])
                self.__pdf.multi_cell(self.__effective_page_width, 7, data)
            else:
                self.__pdf.multi_cell(self.__effective_page_width, 7, f'{ut.cleanText(self.__report_data[content])}')

    def __addImageTextPage(self, content: str) -> None:
        try:
            graph_type = cons.GraphType.behaviour_benchmark if content == 'behaviour_benchmark' else cons.GraphType.competency_benchmark
            graph_image = self.__graph.generateGraph(graph_type=graph_type, benchmark=self.__report_data[content])
            file_name = f'image_{content}_{self.__report_data["role_id"]}_{str(time()).replace(".", "")}.png'
            file_path = os.path.join(cons.TEMP_IMAGE_FILE_PATH, file_name)
            graph_image.save(file_path, 'png')

            image_file = cons.PDF_MID_PAGE_IMAGE
            cover = Image.open(image_file)
            width, height = cover.size
            width, height = float(width * 0.15), float(height * 0.15)
            self.__pdf.add_page()
            self.__pdf.image(image_file, x=0, y=0, w=width, h=height)
            self.__pdf.set_xy(0, 0)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.ln(30)
            self.__pdf.cell(w=1, h=0, txt=f'{content.replace("_", " ").capitalize()}:', border=0, ln=1, align='L')
            self.__pdf.ln(5)
            # Draw Benchmark image
            width, height = graph_image.size
            width, height = float(width * 0.15), float(height * 0.15)
            self.__pdf.image(file_path, x=20, y=50, w=width, h=height)
        except Exception as ex:
            print(f'Graph Generation Failed: {ex}')

    def __addTableData(self, data):
        x_start_position = x_position =self.__pdf.get_x()
        y_start_position = y_position =self.__pdf.get_y()
        self.__pdf.set_font('Arial', '', 10)
        self.__pdf.set_text_color(0, 0, 0)
        for row in data:
            cell_height = cons.CELL_HEIGHT
            max_length = max(len(str(w)) for w in row)
            max_words = max(len(str(w).replace(',', ', ').split()) for w in row)
            max_height = cell_height if max_words < 4 else (max_words/4 + 1) * cell_height
            self.__pdf.set_xy(x_position, y_position)
            width = cons.PAGE_WIDTH/len(row)
            for i, item in enumerate(row):
                # width = 75 if i > 0 else 40
                if max_height <= cell_height:
                    self.__pdf.cell(w=width, h=max_height, txt=' '.join(str(item).capitalize().split('_')), border=1, align='C')
                else:
                    item_lines = len(str(item).replace(',', ', ').split()) / 4
                    item = "\n" * int(max_words/4-item_lines) + item
                    self.__pdf.set_xy(x_position, y_position)
                    self.__pdf.multi_cell(w=width, h=cell_height, txt=item, border=1, align='C')
                    x_position += width
            x_position = x_start_position
            y_position += max_height
        self.__pdf.ln(10)

    def __addMatchingTextPage(self, content: str) -> None:
        image_file = cons.PDF_MID_PAGE_IMAGE
        cover = Image.open(image_file)
        width, height = cover.size
        width, height = float(width * 0.15), float(height * 0.15)
        self.__pdf.add_page()
        self.__pdf.image(image_file, x=0, y=0, w=width, h=height)
        self.__pdf.set_xy(0, 0)
        if content == 'matching_report':
            self.__pdf.set_font('Arial', 'B', 20)
            self.__pdf.ln(100)
            self.__pdf.cell(w=0, h=0, txt='Matching Report', border=0, ln=1, align='C')
            self.__pdf.ln(10)
            self.__pdf.set_font('Arial', 'B', 15)
            self.__pdf.cell(w=0, h=0, txt=f'Role: {ut.cleanText(self.__report_data["role"])}', border=0, ln=1, align='C')
            self.__pdf.ln(7)
            self.__pdf.cell(w=0, h=0, txt='Vs', border=0, ln=1, align='C')
            self.__pdf.ln(7)
            self.__pdf.cell(w=0, h=0, txt=f'Job Seeker: {self.__report_data["candidate"]} (Shortlisted)', border=0, ln=1, align='C')
        elif content == 'vacancy_cv_matching':
            self.__pdf.set_font('Arial', 'B', 12)
            self.__pdf.ln(30)
            self.__pdf.cell(w=0, h=0, txt=f'Role: {ut.cleanText(self.__report_data["role"])} - Job Seeker: {self.__report_data["candidate"]}', border=0, ln=1, align='C')
            self.__pdf.ln(10)
            self.__pdf.set_font('Arial', 'B', 12)
            self.__pdf.set_fill_color(19, 15, 94)
            self.__pdf.set_text_color(255, 255, 255)
            self.__pdf.cell(w=cons.PAGE_WIDTH, h=cons.CELL_HEIGHT, txt='Vacancy and Employee CV Matching', border=0, ln=1, align='C', fill=True)
            self.__pdf.ln(5)
            table_data = [['DESCRIPTION', 'VACANCY REQUIREMENT', 'CANDIDATE CV'],
                          ['Sector', self.__report_data["role_details"]["job_sector"], self.__report_data["candidate_details"]["job_sector"]],
                          ['Job Type', self.__report_data["role_details"]["job_type"], self.__report_data["candidate_details"]["job_type"]],
                          ['Job Function', self.__report_data["role_details"]["job_function"], self.__report_data["candidate_details"]["job_function"]],]
            self.__addTableData(table_data)
        elif content in ['functional_skills', 'technical_skills']:
            self.__pdf.ln(30)
            self.__pdf.set_font('Arial', 'B', 12)
            self.__pdf.set_fill_color(19, 15, 94)
            self.__pdf.set_text_color(255, 255, 255)
            self.__pdf.cell(w=cons.PAGE_WIDTH, h=cons.CELL_HEIGHT, txt=' '.join(content.capitalize().split('_')), border=0, ln=1, align='C', fill=True)
            self.__pdf.ln(5)
            role_skills = self.__report_data["role_details"][content].split(',')
            candidate_skills = self.__report_data["candidate_details"][content].split(',')
            matched_skills = list(set(role_skills).intersection(candidate_skills))
            # role_unmatched_skills = list(set(role_skills) - set(matched_skills))
            # candidate_unmatched_skills = list(set(candidate_skills) - set(matched_skills))
            table_data = [(' ', 'Skills Requested', 'Candidate Specified'),
                          ('Matched', ','.join(matched_skills), ','.join(matched_skills)), ]
                          # ('Unmatched', ','.join(role_unmatched_skills), ','.join(candidate_unmatched_skills))]
            self.__addTableData(table_data)

    def __addImageTablePage(self, content: str, content_data: Dict = None):
        # Get Benchmark/Competency image
        benchmark_data = {}
        try:
            if content == 'behaviour_benchmark':
                graph_type = cons.GraphType.behaviour_benchmark
            elif content == 'competency_benchmark':
                graph_type = cons.GraphType.competency_benchmark
            else:
                graph_type = cons.GraphType.values_benchmark

            if content == cons.GraphType.values_benchmark.name:
                benchmark_data = list(content_data.values())[0]
                title = f'Values Benchmark - {list(content_data.keys())[0]}'
            else:
                role_benchmark_data = self.__report_data['role_details'][content]
                candidate_benchmark_data = self.__report_data['candidate_details'][content]
                if not role_benchmark_data:
                    role_benchmark_data = cons.EMPTY_BEHAVIOUR_BENCHMARK
                if not candidate_benchmark_data:
                    candidate_benchmark_data = cons.EMPTY_COMPETENCY_BENCHMARK
                benchmark_data = {'role': role_benchmark_data, 'candidate': candidate_benchmark_data}
                title = ' '.join(content.capitalize().split('_'))
            graph_image = self.__graph.generateGraph(graph_type=graph_type, benchmark=benchmark_data)
            file_name = f'image_{content}_{str(time()).replace(".", "")}.png'
            file_path = os.path.join(cons.TEMP_IMAGE_FILE_PATH, file_name)
            graph_image.save(file_path, 'png')
        except Exception as ex:
            print(f'Error : {ex}')
            return
        image_file = cons.PDF_MID_PAGE_IMAGE
        cover = Image.open(image_file)
        width, height = cover.size
        width, height = float(width * 0.15), float(height * 0.15)
        self.__pdf.add_page()
        self.__pdf.image(image_file, x=0, y=0, w=width, h=height)
        self.__pdf.set_xy(0, 0)
        self.__pdf.ln(25)
        self.__pdf.set_font('Arial', 'B', 12)
        self.__pdf.set_fill_color(19, 15, 94)
        self.__pdf.set_text_color(255, 255, 255)
        image_width, image_height = graph_image.size
        image_width, image_height = float(image_width * 0.15), float(image_height * 0.15)
        self.__pdf.cell(w=190, h=10, txt=title, border=0, ln=1, align='C', fill=True)
        self.__pdf.image(file_path, x=20, y=35, w=image_width, h=image_height)
        self.__pdf.ln(145)
        # Add comparison table
        # benchmark_keys = self.__report_data['role_details'][content].keys()
        benchmark_data_df = pd.DataFrame(benchmark_data)
        benchmark_data_df['variance'] = benchmark_data_df['role'].apply(int) - benchmark_data_df['candidate'].apply(int)
        benchmark_data_df['variance'] = benchmark_data_df['variance'].apply(str)
        data_columns = ['Competence', *benchmark_data_df.columns]
        data_columns = [item.capitalize() for item in data_columns]
        data_tuples = [data_columns, *list(benchmark_data_df.to_records())]
        self.__addTableData(data_tuples)

    def __addValueGraphs(self):
        graph_name = cons.GraphType.values_benchmark.name
        value_data = ut.constructValuesData(self.__report_data["value_details"])
        if not value_data:
            return
        for item in value_data:
            self.__addImageTablePage(graph_name, item)

    def createVacancyPdf(self) -> str:
        try:
            # Add first page
            self.__addImagePage(cons.VACANCY_PDF_FIRST_PAGE_IMAGE)
            # Add title role page
            self.__addRoleDetailsPage()
            self.__addResponsibiliesPage()
            self.__addSkillsPage()
            self.__addBehaviourBenchmarkPage()
            self.__addCompetencyBenchmarkPage()

            # Add last page
            self.__addImagePage(cons.PDF_LAST_PAGE_IMAGE)
            # Save pfd
            file_name = f'report_{self.__report_data["role_id"]}_{str(time()).replace(".", "")}.pdf'
            file_path = os.path.join(cons.TEMP_IMAGE_FILE_PATH, file_name)
            self.__pdf.output(file_path)
            return file_name
        except Exception as ex:
            print(f'Error : {ex}')
            return f'Error in vacany report pdf generation: {ex}'

    def createMatchingPdf(self) -> str:
        # Add first page
        try:
            self.__addImagePage(cons.MATCHING_PDF_FIRST_PAGE_IMAGE)
            self.__addMatchingTextPage("matching_report")
            self.__addMatchingTextPage("vacancy_cv_matching")
            self.__addMatchingTextPage("functional_skills")
            self.__addMatchingTextPage("technical_skills")
            self.__addImageTablePage("behaviour_benchmark")
            self.__addImageTablePage("competency_benchmark")
            self.__addValueGraphs()

            # Save pfd
            file_name = f'report_matching_{str(time()).replace(".", "")}.pdf'
            file_path = os.path.join(cons.TEMP_IMAGE_FILE_PATH, file_name)
            self.__pdf.output(file_path)
            return file_name
        except Exception as ex:
            print(f'Error : {ex}')
            return f'Error in matching pdf generation: {ex}'


def main(report_json):
    gen_pdf = PdfGenerator(report_json)
    print(gen_pdf.createVacancyPdf())
    # print(gen_pdf.createMatchingPdf())


if __name__ == '__main__':
    from Test.testData import matching_json, vacancy_json
    # data_json = json.loads(matching_json, strict=False)
    data_json = json.loads(vacancy_json, strict=False)
    print(f'Type: {type(data_json)}')
    print(data_json)
    main(data_json)
