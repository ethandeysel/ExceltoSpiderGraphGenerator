import pandas as pd
import numpy as np
import re

def process_wheel_data(uploaded_file):
    # load data
    data = pd.read_excel(uploaded_file, index_col=0,header=1)
    data = np.round(data,1)
    df = data.copy()
    # cleaning 
    df = df.iloc[:, :4] 
    df.columns = ['Variable', 'Control_Name', 'Status', 'Score/5'] 
    df = df.dropna(subset=['Score/5'])
    df['Variable'] = df['Variable'].astype(str)
    df['Control_Name'] = df['Control_Name'].astype(str)
    df['Status'] = df['Status'].astype(str).str.strip().str.lower()
    df['Score/5'] = pd.to_numeric(df['Score/5'], errors='coerce')

    # Extract the control group prefix
    df['Group'] = df['Variable'].apply(lambda x: '.'.join(x.split('.')[:2]))
    pattern = r'^[A-Z]\.\d+$'
    mask = df['Group'].str.match(pattern, na=False)
    df = df[mask].copy()
    return df