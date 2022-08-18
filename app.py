import flask
from flask import Flask
from flask_cors import CORS
import json
import os
from time import time
import requests
from PdfGenerator import PdfGenerator
from GraphGenerator import GraphGenerator
import Constants as cons
from Utils import Utils as ut

WEB_IP_ADR = '0.0.0.0'
app = Flask(__name__)
CORS(app)


def createGraphImageFile(username: str, graph_name: str, api_url: str) -> str:
    response = requests.get(url=api_url)
    data = response.json()
    print(data)

    img_obj = GraphGenerator()
    if graph_name == cons.GraphType.values_benchmark.name:
        value_data = ut.constructValuesData(data)
        graph_paths = []
        for item in value_data:
            item_key = list(item.keys())[0]
            item_value = list(item.values())[0]
            b_graph = img_obj.generateGraph(graph_type=cons.GraphType[graph_name], benchmark=item_value)
            file_name = f'image_{username}_{graph_name}_{str(time()).replace(".", "")}.png'
            file_path = os.path.join(cons.TEMP_IMAGE_FILE_PATH, file_name)
            b_graph.save(file_path, 'png')
            graph_paths.append({'name': item_key, 'image': file_name})
        return json.dumps(graph_paths)
    else:
        b_graph = img_obj.generateGraph(graph_type=cons.GraphType[graph_name], benchmark=data)
        file_name = f'image_{username}_{graph_name}_{str(time()).replace(".", "")}.png'
        file_path = os.path.join(cons.TEMP_IMAGE_FILE_PATH, file_name)
        b_graph.save(file_path, 'png')
        return json.dumps(file_name)


def getBaseUrl(graph_name: str) -> str:
    if graph_name == cons.GraphType.behaviour_benchmark.name:
        return cons.REST_API_BEHAVIOUR_DATA_URL
    elif graph_name == cons.GraphType.competency_benchmark.name:
        return cons.REST_API_COMPETENCY_DATA_URL
    elif graph_name == cons.GraphType.values_benchmark.name:
        return cons.REST_API_VALUES_DATA_URL
    else:
        raise ValueError(f'Couldnt find graph type:{graph_name}')


@app.route('/healthcheck', methods=['GET'])
def healthCheck() -> str:
    return 'I am okay'


@app.route('/api/reports/pdf/vacancy/<username>/<vacancyid>', methods=['GET'])
def generateVacancyReport(username: str, vacancyid: str) -> str:
    try:
        api_url = f'{cons.REST_API_VACANCY_DATA_URL}/{username}/{vacancyid}'
        response = requests.get(url=api_url)
        data = response.json()
        gen_pdf = PdfGenerator(data)
        file_path = gen_pdf.createVacancyPdf()
        return file_path
    except Exception as ex:
        flask.abort(404, description=ex)


@app.route('/api/reports/pdf/matching/<username>/<vacancyid>/<jobseekerid>', methods=['GET'])
def generateMatchingReport(username: str, vacancyid: str, jobseekerid: str) -> str:
    try:
        api_url = f'{cons.REST_API_MATCHING_DATA_URL}/{username}/{vacancyid}/{jobseekerid}'
        response = requests.get(url=api_url)
        data = response.json()
        gen_pdf = PdfGenerator(data)
        file_path = gen_pdf.createMatchingPdf()
        return file_path
    except Exception as ex:
        flask.abort(404, description=ex)


@app.route('/api/reports/graph/<username>/<graphtype>', methods=['GET'])
def generateJobseekerGraph(username: str, graphtype: str):
    try:
        base_url = getBaseUrl(graphtype)
        api_url = f'{base_url}/{username}'
        return createGraphImageFile(username, graphtype, api_url)
    except Exception as ex:
        flask.abort(404, description=ex)


@app.route('/api/reports/graph/<username>/<vacancyid>/<graphtype>', methods=['GET'])
def generateVacancyGraph(username: str, graphtype: str, vacancyid: str):
    try:
        base_url = getBaseUrl(graphtype)
        api_url = f'{base_url}/{username}/{vacancyid}'
        return createGraphImageFile(username, graphtype, api_url)
    except Exception as ex:
        flask.abort(404, description=ex)

@app.route('/api/reports/graph/<username>/<vacancyid>/<jobseekerid>/<graphtype>', methods=['GET'])
def generateMatchingGraph(username: str, graphtype: str, vacancyid: str, jobseekerid: str) -> str:
    try:
        base_url = getBaseUrl(graphtype)
        api_url = f'{base_url}/{username}/{vacancyid}/{jobseekerid}'
        return createGraphImageFile(username, graphtype, api_url)
    except Exception as ex:
        flask.abort(404, description=ex)


def runService() -> None:
    """
    Entry-level for the service invocation
    :return: None
    """
    app.debug = True
    app.run(host=WEB_IP_ADR, port=9090, processes=True)


if __name__ == '__main__':
    runService()


