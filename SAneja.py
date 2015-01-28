from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv


main_dir = "/Users/saurabh/Desktop/Github"
txt_file = "/Data/File1_small.txt"

saurabh = read_table(File1_small.txt)

f = open(File1_small.txt, '')
try:
    reader = csv.DictReader(f)
    for row in reader:
        print row
finally:
    f.close()
