"""
Tests for `aviio_technical_component` module.
"""

import json
import os
import pytest
import pandas as pd
from pathlib import Path
from aviio_technical_component.aviio_technical_component import structure_data, save_to_csv


class TestAviio_technical_component(object):
    test_dir = Path(__file__).absolute().parent

    @classmethod
    def load_json(cls, json_path):
        with open(json_path) as f:
            data = json.load(f)

        return data

    def test_structure_data(self):
        file_path = self.test_dir / "test_data" / "example_response.json"
        test_data = self.load_json(file_path)
        dataframe = structure_data(test_data)
        payout_list = dataframe['payout'].to_list()
        assert payout_list == sorted(payout_list)

    def test_save_to_csv(self, tmpdir):
        dataframe = pd.DataFrame()
        output_dir = tmpdir / "test_data"
        output_path = save_to_csv(dataframe, output_dir)
        assert os.path.exists(output_path)
