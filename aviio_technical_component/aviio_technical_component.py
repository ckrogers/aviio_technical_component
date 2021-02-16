import logging
import os
import pandas as pd
from pathlib import Path

logging.basicConfig(filename='aviio_technical_component.log', encoding='utf-8', level=logging.DEBUG)
package_dir = Path(__file__).parent.absolute()


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

def save_to_csv(dataframe, output_dir: None):
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
    logging.info(f'Data saved to path: {csv_path}')
    return csv_path

if __name__ == "__main__":
    pass
