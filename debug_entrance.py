from canoeClass import data_process
import configparser


config = configparser.ConfigParser()
config.read("source.conf", encoding="utf-8")

case_file = config.get("file", "casefile")

datapro = data_process.DataProcess(case_file)

result = datapro.extract_sig_val()
