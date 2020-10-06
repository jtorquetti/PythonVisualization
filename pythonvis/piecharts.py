import matplotlib.pyplot as pt
import pandas as pd

data = pd.read_csv("pythonvis/cgpa.csv")
data = data.head(30)
x = len(data[data.cgpa>=9])
x1 = len(data[data.cgpa>=8])
x2 = len(data[data.cgpa<8])
pt.axis("equal")

pt.pie([x,x1,x2], colors=["yellow", "red","blue"], labels=["9 pointer", "8 pointer", "others"])
pt.legend(title='Description')
pt.show()