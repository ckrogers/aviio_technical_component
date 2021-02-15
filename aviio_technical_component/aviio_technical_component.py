import pandas as pd


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
