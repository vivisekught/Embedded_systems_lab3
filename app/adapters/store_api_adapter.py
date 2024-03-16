from typing import List

import requests

from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_gateway import StoreGateway


class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def _get_url(self):
        return f"{self.api_base_url}/processed_agent_data/"

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]):
        url = self._get_url()
        data = []
        for model in processed_agent_data_batch:
            data.append(model.model_dump_json())
        parsed_data = '[' + ','.join(data) + ']'
        headers = {'Content-Type': 'application/json'}

        res = requests.post(url, data=parsed_data, headers=headers)

        if res.status_code == 200:
            return True
        else:
            return False
