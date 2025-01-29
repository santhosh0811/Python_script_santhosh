import pandas as pd
import json



def read_excel_content(excel_file_path,json_file_path):
    df=pd.read_excel(excel_file_path,sheet_name="Sheet1")
    #print(df)
    df1=df.applymap(lambda x: x.strip() if isinstance(x, str) else x )
    df1.to_json(json_file_path, orient='records', indent=4)

    print("excel file converted into json file")






excel_file_path="/home/ubuntu/python/day28/python/sample.xlsx"


json_file_path="xyz.json"

read_excel_content(excel_file_path,json_file_path)
