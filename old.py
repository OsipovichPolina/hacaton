import pandas as pd
import numpy as np
from datetime import datetime, timedelta

df = pd.read_csv(r'C:\Users\homep\Downloads\hackathon\mer_train_fin1.csv', sep=';')
cat = pd.read_csv(r'C:\Users\homep\Downloads\hackathon\cat_dur.csv', sep=';')
print(df.dtypes)
df["real_time"] = pd.to_datetime(df["real_time"], format='%Y-%m-%d %H:%M:%S')
print(df.shape[0])
start_date = datetime(2021, 8, 2, hour=0, minute=0, second=0, microsecond=0)
end_date = datetime(2021, 8, 8, hour=23, minute=59, second=59, microsecond=59)
city = "Новосибирск"
osv = "10.0"

df = df.query('city == @city and osv == @osv and real_time >= @start_date and real_time <= @end_date')
df = df.sort_values(by=["category", "real_time"])
print(df.shape[0])

df.reset_index(drop=True, inplace=True)
print(df.head())


count_cat = cat.shape[0]
for cc in range(count_cat):
    y = int(cat.at[cc, 'uses'])
    x = int(cat.at[cc, 'ad'])
    count_y = int(60*24*7 / y)
    count_x = int(y/x)
    save_index = 0
    t1 = start_date
    t2 = start_date + timedelta(minutes=x)
    end_ind = df.shape[0]
    maxx = []
    count_in_cat = 0
    for i in range(count_y):
        s = []
        for j in range(count_x):
            sx = 0
            start_ind = save_index

            for k in range(start_ind, end_ind):
                if df.at[k, 'category'] != cat.at[cc, 'category']:
                    continue

                if df.at[k, 'real_time'] >= t2:
                    break
                if t1 <= df.at[k, 'real_time'] < t2:
                    sx += 1
                    count_in_cat += 1
                    save_index = k
            t1 = t2
            t2 = t2 + timedelta(minutes=x)
            s.append(sx)

        maxx.append(max(s, default=0))

    print(""+cat.at[cc, 'category']+" " + str(count_in_cat)+" "+str(sum(maxx)))