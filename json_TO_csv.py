import pandas as pd
df = pd.read_json (r'JSON_Data_v.5.json',lines=True)
df.to_csv (r'RTW.csv', index = None)