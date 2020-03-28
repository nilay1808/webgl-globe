import sys
import csv
import pandas as pd
from datetime import date
from datetime import timedelta
import json
import math


def main():
    base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
    d = (date.today() - timedelta(days=1)).strftime("%m-%d-%Y")
    url = base_url + d + ".csv"

    df = pd.read_csv(url, error_bad_lines=False)
    # print(df)

    data = []

    confirmed = ["confirmed"]
    confirmed_data = []

    deaths = ["death"]
    deaths_data = []

    recovered = ["recovere"]
    recovered_data = []

    for index, row in df.iterrows():
        # Add to Confirmed
        if row["Confirmed"] != 0:
            confirmed_data.append(row["Lat"])
            confirmed_data.append(row["Long_"])
            confirmed_data.append((math.log10(row["Confirmed"]) * 0.225) ** 2)

        # Add to Deaths
        deaths_data.append(row["Lat"])
        deaths_data.append(row["Long_"])
        deaths_data.append(row["Deaths"])
            
        # Add to Recovered
        recovered_data.append(row["Lat"])
        recovered_data.append(row["Long_"])
        recovered_data.append(row["Recovered"])

    confirmed.append(confirmed_data)
    deaths.append(deaths_data)
    recovered.append(recovered_data)

    data.append(confirmed)
    data.append(deaths)
    data.append(recovered)

    # print(json.dumps(data))

    with open("./globe/population.json", "w") as file:
        json.dump(data, file)


if __name__ == '__main__':
    main()
