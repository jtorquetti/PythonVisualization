import matplotlib.pyplot as pt
import pandas as pd

data = pd.read_csv("pythonvis/cgpa.csv")
data = data.head(40)

pt.scatter(data["rollno"],data["cgpa"], color="blue", label="scatter")

pt.xlabel("RollNo", color="green")
pt.ylabel("CGPA", color="blue")
pt.title("CGPA vs Roll No", color="green")
pt.plot(data["rollno"], data["cgpa"], color="red",label="line graph")
pt.legend()

pt.show()

