
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x =['18-44','45-54','55-64','65-74','75 years and over']
y =['0.9','5.1','10.7','18.3','24.1']

data1 = pd.read_excel('HDPrv.xlsx')


plt.scatter(x,y)
plt.xlabel("Age")
plt.ylabel("Percentage of Population with Heart Disease")
plt.savefig("the_graph.png")
plt.show()