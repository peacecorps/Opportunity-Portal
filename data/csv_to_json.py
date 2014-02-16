import pandas as pd
import json


df = pd.read_csv('data/pc.csv',encoding = "ISO-8859-1")
jobs = []

for row_idx, row in df.iterrows():
    job = {}

    print row['POST'].isnan
    job['current_req_status'] = row['CURRENT REQ STATUS'] if row['CURRENT REQ STATUS'] else None
    job['FY'] = row['FY'] if row['FY'] else None
    job['Q'] = row['Q'] if row['Q'] else None
    job['AA'] = row['AA'] if row['AA'] else None
    job['location'] = row['POST'] if row['POST'] else None
    job['REQ ID'] = row['REQ ID'] if row['REQ ID'] else None
    job['num_vol'] = row['# VOL REQUESTED'] if row['# VOL REQUESTED'] else None
    job['title'] = row['PROJECT TITLE'] if row['PROJECT TITLE'] else None
    job['language'] = row['LANG'] if row['LANG'] else None
    job['sector'] = row['SECTOR'] if row['SECTOR'] else None
    job['nominate_deadline'] = row['LAST DATE TO NOMINATE'] if row['LAST DATE TO NOMINATE'] else None
    job['invite_deadline'] = row['INVITATION DEADLINE'] if row['INVITATION DEADLINE'] else None
    job['STAGING'] = row['STAGING'] if row['STAGING'] else None
    job['live_cond'] = row['Living Conditions [Living_Cond]'] if row['Living Conditions [Living_Cond]'] else None
    job['live_cond_comm'] = row['Living Conditions Comments [Condition_Comments]'] if row['Living Conditions Comments [Condition_Comments]'] else None
    job['skills'] = row['Desired Skills [Desired_Skills]'] if row['Desired Skills [Desired_Skills]'] else None
    job['proj_desc'] = row['Project Description [Project_Description]'] if row['Project Description [Project_Description]'] else None

    jobs.append(job)



with open('data/pc.json', 'w') as f:
    json.dump(jobs, f)
