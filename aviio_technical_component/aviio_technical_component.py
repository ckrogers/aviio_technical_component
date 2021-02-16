import logging
import os
import pandas as pd
from pathlib import Path
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("aviio_technical_component.log", "w", "utf-8")
logger.addHandler(handler)

package_dir = Path(__file__).parent.absolute()
API_TOKEN = os.getenv("TOKEN")
API_URL = "https://atlas.pretio.in/atlas/coding_quiz"


def get_data_from_api():
    retry_strategy = Retry(
        total=1,
        status_forcelist=[429],
        method_whitelist=["HEAD", "GET"],
        backoff_factor=60,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    result = session.get(API_URL, headers={"Authorization": f"Bearer {API_TOKEN}"})
    result.raise_for_status()

    return result.json()


def structure_data(data):
    """
    Structure json data from API_URL to dataframe
    Sort data by ascending payout.
    """
    offers_list = data["rows"]
    df = pd.DataFrame(offers_list)
    df[["cap", "payout"]] = df[["cap", "payout"]].apply(pd.to_numeric, errors="ignore")
    df_sorted = df.sort_values(by="payout", ascending=True)
    df_sorted.reset_index(drop=True, inplace=True)
    return df_sorted


def save_to_csv(dataframe, output_dir=None):
    """
    Save pandas dataframe to .csv
    """
    csv_filename = "offers.csv"
    if not output_dir:
        output_dir = package_dir / "data"

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    csv_path = output_dir / csv_filename
    dataframe.to_csv(csv_path, index=False)
    message = f"Data saved to path: {csv_path}"
    print(message)
    logging.info(message)
    return csv_path


if __name__ == "__main__":
    offers_data = get_data_from_api()
    structured_data = structure_data(offers_data)
    path = save_to_csv(structured_data)
