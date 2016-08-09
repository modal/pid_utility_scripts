import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import sys
style.use("ggplot")
#print(plt.style.available)

print "Pandas", pd.__version__

xlsx=0
if len(sys.argv) == 1:
    xlsx=pd.ExcelFile("ngc20160617_09_04_09out(CRM004 Kp=10, kd=63rd, ki=125th).xlsx")
else:
    xlsx=pd.ExcelFile(sys.argv[1])

#xlsx=pd.ExcelFile("test.xlsx")
df=pd.read_excel(xlsx, 'Sheet1', engine='python')#, engine='xlrd')
df.set_index("time", inplace=True)
#print df.head()
#

#toi= ["beam_i", "rep_i", "beam_i_sp", "br_dac", "beam_i_filtered"]
#df[toi].plot(title="Test", sharey=False, legend=True, secondary_y=True)

df["rep_i"].plot(legend=True, secondary_y=True)#, subplots=True, layout=(2,-1))
df["beam_i"].plot(title="TEST",sharey=False, legend=True)
df["beam_i_sp"].plot(legend=True)
df["br_dac"].plot(legend=True)
df["beam_i_filtered"].plot(legend=True)

plt.show()
