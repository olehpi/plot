import sys
from pathlib import Path

from com.science.graph import DataProcessing as data_processing

file_name = str(Path(__file__).parent / "project" / "data.json")
data = data_processing.DataProcessing(file_name, decimal=".")
data.data_shows()
sys.exit()
