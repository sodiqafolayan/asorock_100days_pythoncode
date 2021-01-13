import pandas as pd
import time

bank_data = pd.read_csv("651_m3_datasets_v1.0/bank-data.csv")
#print(bank_data.head(20))
eligible_jobs = ["management", "blue-collar", "admin"]

job = input("What is the prospective client profession? ")
if job.lower() in eligible_jobs:
    print(f"A prospective client with the job role '{job.title()}' is eligible")
else:
    print("Not eligible")
    time.sleep(1)
    print("Below are the list of eligible roles")
    for item in eligible_jobs:
        print(item.title())

