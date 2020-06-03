import os
import pandas as pd
import csv
from pathlib import Path

path = Path(__file__).parent.absolute()
file_path = os.path.join(path, "..", "telecom_churn.csv")
outfile_path = os.path.join(path, "..", "output.csv")


def analysed_data():
    ds = pd.read_csv(file_path)
    mode = "a" if os.path.exists(outfile_path) else "w"
    with open(outfile_path, mode) as output_file:
        out = csv.writer(output_file)
        out.writerow(["Parameter", "Count", "Churn", "Not Churn"])

        ds1 = ds[ds["ContractRenewal"] == 0]
        ds2 = ds1[ds1["Churn"] == 0].shape[0]
        ds3 = ds1[ds1["Churn"] == 1].shape[0]
        out.writerow(["Customers who didn't renewed contracts", ds1.shape[0], ds2, ds3])

        ds1 = ds[ds["ContractRenewal"] == 1]
        ds2 = ds1[ds1["Churn"] == 0].shape[0]
        ds3 = ds1[ds1["Churn"] == 1].shape[0]
        out.writerow(
            ["Customers who recently renewed contracts", ds1.shape[0], ds2, ds3]
        )

        ds1 = ds[ds["DataPlan"] == 0]
        ds2 = ds1[ds1["Churn"] == 0].shape[0]
        ds3 = ds1[ds1["Churn"] == 1].shape[0]
        out.writerow(["Customers without data plan", ds1.shape[0], ds2, ds3])

        ds1 = ds[ds["DataPlan"] == 1]
        ds2 = ds1[ds1["Churn"] == 0].shape[0]
        ds3 = ds1[ds1["Churn"] == 1].shape[0]
        out.writerow(["Customers with data plan", ds1.shape[0], ds2, ds3])

        ds1 = ds[ds["DataUsage"] == 0]
        ds2 = ds1[ds1["Churn"] == 0].shape[0]
        ds3 = ds1[ds1["Churn"] == 1].shape[0]
        out.writerow(["Customers with 0 data usage", ds1.shape[0], ds2, ds3])

        ds1 = ds[ds["DataUsage"] > 0]
        ds2 = ds1[ds1["Churn"] == 0].shape[0]
        ds3 = ds1[ds1["Churn"] == 1].shape[0]
        out.writerow(["Customers with data usage", ds1.shape[0], ds2, ds3])
