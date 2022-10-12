from canoeClass import data_process
import configparser


config = configparser.ConfigParser()
config.read("source.conf", encoding="utf-8")
dbc_files = config.get("file", "dbcfiles").split(",")

case_file = config.get("file", "casefile")

datapro = data_process.DataProcess(case_file)

parsedbc={}
for dbc_file in dbc_files:
    dbc = data_process.DBCload(dbc_file)
    dict_dbc = dbc.parseDBC()
    parsedbc = dict(**parsedbc, **dict_dbc)

result = datapro.extract_sig_val(parseDBC=parsedbc)

# result2 = datapro.get_wait_time("wait 3s")

print(result)