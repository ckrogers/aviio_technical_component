"""
Tests for `aviio_technical_component` module.
"""

import pytest
import json
import os
import httpretty
import pandas as pd
from pathlib import Path
import requests_mock
from requests import HTTPError
from aviio_technical_component.aviio_technical_component import (
    API_URL,
    get_data_from_api,
    structure_data,
    save_to_csv,
)


class TestAviio_technical_component(object):
    test_dir = Path(__file__).absolute().parent

    @classmethod
    def load_json(cls, json_path):
        with open(json_path) as f:
            data = json.load(f)

        return data

    def test_structure_data(self):
        """Assert data is structured and sorted by 'payout' column"""
        file_path = self.test_dir / "test_data" / "example_response.json"
        test_data = self.load_json(file_path)
        dataframe = structure_data(test_data)
        payout_list = dataframe["payout"].to_list()
        assert payout_list == sorted(payout_list)

    def test_save_to_csv(self, tmpdir):
        """Assert csv is saved to path provided"""
        dataframe = pd.DataFrame()
        output_dir = tmpdir / "test_data"
        save_to_csv(dataframe, output_dir)
        assert os.path.exists(output_dir / "offers.csv")

    def test_error_500(self, requests_mock):
        """Assert error is raised when faced with 500 error from call to API endpoint"""
        requests_mock.get(API_URL, status_code=500, text="fake server error.")
        with pytest.raises(HTTPError):
            get_data_from_api()

    @httpretty.activate
    def test_error_429(self):
        """Assert call to API endpoint is retried when faced with a 429 error"""
        file_path = self.test_dir / "test_data" / "example_response.json"
        test_data = self.load_json(file_path)
        mock_token = "fndsofbosabo"
        httpretty.register_uri(
            httpretty.GET,
            API_URL,
            adding_headers={"Authorization": f"Bearer {mock_token}"},
            # adding_headers={'Authorization': API_TOKEN},
            responses=[
                httpretty.Response(
                    body="{}",
                    status=429,
                ),
                httpretty.Response(
                    body=json.dumps(test_data),
                    status=200,
                ),
            ],
        )

        resp = get_data_from_api()
        request_num = len(httpretty.latest_requests())
        assert request_num == 2
