import pandas as pd
import re
from typing import List, Dict
from Constants import null


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def constructValuesData(values_data):
        value_nodes = []
        if not values_data:
            return value_nodes
        try:
            jobseeker_values = values_data[0]
            company_values = values_data[1:]
            company_values_df = pd.DataFrame(company_values)
            value_constructs = company_values_df.value_name.unique()
            for construct in value_constructs:
                condition = company_values_df.value_name == construct
                construct_df = company_values_df[condition].groupby('behaviour_name').mean('behaviour_score').reset_index()[
                    ['behaviour_name', 'behaviour_score']]
                role_dict = {item[1][0]: item[1][1] for item in construct_df.iterrows()}
                role_keys = role_dict.keys()
                if jobseeker_values:
                    jobseeker_dict = {k: jobseeker_values[k] for k in role_keys}
                    node = {construct: {'role': role_dict, 'candidate': jobseeker_dict}}
                else:
                    node = {construct: {'role': role_dict}}
                value_nodes.append(node)
        except Exception as ex:
            print(f"Error: {ex}")
        return value_nodes

    @staticmethod
    def cleanText(text: str) -> str:
        if not text:
            return ''
        text = text.replace(',', ', ')
        text = text.replace('\n', ' ')
        text = text.replace('  ', ' ')
        text = text.encode('latin-1', 'replace').decode('latin-1')
        return re.sub(r'[^\x00-\x7F]+', ' ', text)

