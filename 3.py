import pandas as pd
file='/home/yogesh/Desktop/extra/USA 340_Delivery Metadata_Kannada_Batch 13.csv'
view=pd.read_csv(file)
view.drop_duplicates(inplace=True)
print(view.info())