from http.client import responses

import requests
from utils import Utils_1
class Api_Client:

    base_url = Utils_1.BASE_URL

    def __init__(self):
        self.headers = {
            "Content-type" : "application/json"
        }

    def get(self, endpoint, headers=None):
        headers_copy = self.headers.copy()
        if headers:
            headers_copy.update(headers)
        get_response = requests.get(self.base_url+endpoint, headers=headers_copy, timeout=5)
        return get_response

    def post(self, endpoint, payload, headers=None):
        header_copy = self.headers.copy()
        if headers:
            header_copy.update(headers)
        post_response = requests.post(self.base_url+endpoint,headers=header_copy,json=payload, timeout=5)
        return post_response

    def put(self, endpoint, payload, headers=None):
        try:
            header_copy = self.headers.copy()
            if headers:
                header_copy.update(headers)
            patch_response = requests.put(self.base_url+endpoint, headers=self.headers, json=payload, timeout=5)
            return patch_response
        except ConnectionError as e:
            print(f"Connection error : {e}")


    def delete(self, endpoint):
        delete_response = requests.delete(self.base_url+endpoint, headers=self.headers, timeout=5)
        return delete_response

