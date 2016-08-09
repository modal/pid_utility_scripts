"""
This script converts space(s) separated value file to an xlsx file.

Prerequistes:
    Pandas
    xlrd
    openpyxl
"""
##############################################################################
import pandas as pd
import  sys

if len(sys.argv) < 2:
    sys.exit()

for fn in sys.argv[1:]:
    #print fn
    df = pd.read_csv(fn,  delimiter=r"\s*", index_col=0, engine='python')
    #print df
    df.to_excel(fn[:-4] + ".xlsx", sheet_name='Sheet1')
