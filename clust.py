import pandas as pd


df = pd.read_csv(r'C:\Users\homep\Downloads\hackathon\test_pred.csv', sep=',')
coeff = pd.read_csv(r'C:\Users\homep\Downloads\hackathon\coeff.csv', sep=';')
df.drop(df.columns[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]], inplace=True, axis=1)
df['count_clust'] = df['Segment']
df.groupby(['Segment', 'category'], as_index=False).aggregate({'count_clust': 'count'})

mer = df.merge(coeff, on=['category'], how='left')
mer = mer[mer['Segment'].notna()]
mer = mer[mer['category'].notna()]
mer['people'] = mer.apply(lambda row: int(int(row['count_clust']) * float(row['coeff'])), axis=1)


mer.drop(mer.columns[[0, 1, 3, 4]], inplace=True, axis=1)
mer = mer.groupby(['Segment'], as_index=False).aggregate({'people': 'sum'})
mer.to_csv('people.csv')
