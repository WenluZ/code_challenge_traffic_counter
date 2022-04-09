import pandas as pd

#generate test cases
def create_df():
    data = {'timestamp':['2021-12-05T15:30:00', '2021-12-08T18:00:00', '2021-12-08T18:30:00', '2021-12-08T19:00:00'], 'count':[5, 10, 0, 15]}  
    df = pd.DataFrame(data)  
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%dT%H:%M:%S')
    df['count'] = df['count'].astype('int')

    return df 




