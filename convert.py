import pandas as pd
import numpy as np
data= pd.read_csv('datacsv\datapola3\925213.csv').drop([ 'Unnamed: 0','label' ],axis=1)/1000
data.columns= [np.arange(0,8)]
data.to_csv(f"templates/data.csv")
print(data)