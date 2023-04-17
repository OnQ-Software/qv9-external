import pandas as pd
from qlims.bridge import BridgeOutput
import sys
import pymssql


def my_logic(file_name):
        datacsv = pd.read_csv(file_name)
        batchId = datacsv.columns[1]
        conn = pymssql.connect('CONNECTION_DETAILS')
        sql_query = "SQL_QUERY_STRING"
        df = pd.read_sql_query(sql_query, conn)
        conn.close()
        sets = {}
        param = datacsv.iloc[0].values.flatten().tolist()
        runNumbers = datacsv.iloc[:, 0:1].values.flatten().tolist()
        Bridge = BridgeOutput()
        arraycsvdata = []
        for i in range(len(runNumbers)):
            if i != 0:
                value = datacsv.iloc[i].values.flatten().tolist()
                for pa in range(len(param)):
                    if pa != 0:
                        finaloutput = df.query("RUN_NO == " + value[0] + "and PA_NAME == '" + param[pa] + "'")
                        finaloutput = finaloutput.values
                        for out in finaloutput:
                            if {"SAMPLE_ID": out[2], "PA_NAME": out[0], "SRESULT": value[pa],
                                "RUN_NO": value[0]} not in arraycsvdata:
                                sets["SRESULT"] = value[pa]
                                Bridge.add_update_sample_parameter_operation(
                                    {"SAMPLE_ID": out[2], "PA_NAME": out[0]},
                                    sets)
                                sets = {}
                                arraycsvdata.append(
                                    {"SAMPLE_ID": out[2], "PA_NAME": out[0], "SRESULT": value[pa], "RUN_NO": value[0]})
        Bridge.output_message = "Updating values for Sample  from Bridge. " + "Status: Successfully Updated"
        Bridge.print()