import json

import pytest
from datetime import datetime
import os


@pytest.hookimpl(tryfirst=True)
def report_format(config):
    folder_path = "reports"
    current_date_and_time = datetime.now().strftime("%Y-%M-%D_%H-%M-%S")
    config.option.htmlpath = f"{folder_path}/report_{current_date_and_time}.html"

@pytest.fixture
def load_json_file():
    file_path = os.path.join(os.path.dirname(__file__),"data","payload_data.json")
    with open(file_path) as json_file:
        json_data = json.load(json_file)
        return json_data