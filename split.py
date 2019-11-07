import pandas as pd 
import os

dir_name = ''
file_count = sum([len(files) for r, d, files in os.walk(dir_name)])
print(file_count)