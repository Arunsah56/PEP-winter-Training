import pandas as pd
data = pd.read_json("http://127.0.0.1:8000/api/books/?format=json")
print(data)