import pandas as pd
i = "2022- 11- 29"
df = pd.read_csv(r'C:\Users\최민호\PycharmProjects\AIacademy-django-react\djangoProject\aitrader\data\samsung.csv')
df2 =  df[df['날짜'] == i]
df3 = df2.index
print(df3[0])
print(type(df3[0]))
# print(df[df['날짜'] == "2021- 01- 04"])