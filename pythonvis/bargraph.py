import matplotlib.pyplot as pt
import pandas as pd

data = pd.read_csv("pythonvis/cgpa.csv")

data = data.head(30)
pt.bar(data["rollno"], data["cgpa"], color=["green","blue","pink","red"])
pt.xlabel("RollNo", color="green")
pt.ylabel("CGPA", color="blue")
pt.title("CGPA vs Roll No", color="green")
pt.show()
