import pandas as pd
df=pd.read_csv(r"the/path/to/the/original/sequence/download/summary/table",low_memory=False)
df['Collection_Date']=pd.to_datetime(df['Collection_Date'])
df.index=df['Collection_Date']
del df['Collection_Date']
df=df.sort_index()
df1=df.drop_duplicates(subset=['Pangolin'],keep='first')
df1=df1.reset_index()
df1.to_csv(r"the/path/to/the/new/generated/ table")
