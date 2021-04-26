
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data/World/time_series_covid_19_confirmed.csv")
df = df.rename(columns={"Country/Region": "Country",
               "Province/State": "Province"})

total_list = df.groupby('Country')['4/13/20'].sum().tolist()

country_list = df["Country"].tolist()
country_set = set(country_list)
country_list = list(country_set)
country_list.sort()

new_df = pd.DataFrame(list(zip(country_list, total_list)),
                      columns=['Country', 'Total_Cases'])
