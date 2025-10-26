import sys
from com.science.graph import DataProcessing as data_processing

file_name = "E:\\A\\TransportSystem\\src\\main\\resources\\org\\sb\\control\\engine\\async\\project\\data.json"
data = data_processing.DataProcessing(file_name, decimal=".")
data.data_shows()
sys.exit()
