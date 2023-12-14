import pandas as pd
from elasticsearch import Elasticsearch


def indexing():
    df = pd.read_csv('final_df.csv')
    es = Elasticsearch("http://localhost:9200")
    for i, row in new_df.iterrows():
        row = row.fillna('')
        doc = {
            "Job Id": row["Job Id"],
            "Experience": row["Experience"],
            "Qualifications": row["Qualifications"],
            "Salary Range": row["Salary Range"],
            "location": row["location"],
            "Country": row["Country"],
            "latitude": row["latitude"],
            "longitude": row["longitude"],
            "Work Type": row["Work Type"],
            "Company Size": row["Company Size"],
            "Job Posting Date": row["Job Posting Date"],
            "Preference": row["Preference"],
            "Contact Person": row["Contact Person"],
            "Contact": row["Contact"],
            "Job Title": row["Job Title"],
            "Role": row["Role"],
            "Job Portal": row["Job Portal"],
            "Job Description": row["Job Description"],
            "Benefits": row["Benefits"],
            "skills": row["skills"],
            "Responsibilities": row["Responsibilities"],
            "Company": row["Company"],
            "Company Profile": row["Company Profile"]
        }

        es.index(index="job_intern", id=i, document=doc)
