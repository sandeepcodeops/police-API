import pandas as pd
import plotly.express as px

import seaborn as sns
import matplotlib.pyplot as plt

import missingno

sns.set_theme(style="darkgrid")

data = pd.read_csv('netflix_titles.csv')
# print(data.head())

# missing values bar graph
color = ['dimgrey', 'dimgrey', 'dimgrey', 'red', 'maroon', 'maroon', 'dimgrey', 'dimgrey', 'dimgrey', 'dimgrey', 'dimgrey', 'dimgrey']
missingno.bar(data,fontsize=10,color=color,figsize=(8,5))
plt.title('MISSING VALUES', fontsize=20)
plt.show()

data['country'] = data['country'].fillna(data['country'].mode()[0])
data['date_added'] = data['date_added'].fillna(data['date_added'].mode()[0])
data['rating'] = data['rating'].fillna(data['country'].mode()[0])

data.drop(['cast', 'director'], axis='columns', inplace=True)

data['y_add'] = data['date_added'].apply(lambda x: x.split(" ")[-1])
data['m_add'] = data['date_added'].apply(lambda x: x.split(" ")[0])

ratings_ages = {
    'TV-PG': 'Older Kids',
    'TV-MA': 'Adults',
    'TV-Y7-FV': 'Older Kids',
    'TV-Y7': 'Older Kids',
    'TV-14': 'Teens',
    'R': 'Adults',
    'TV-Y': 'Kids',
    'NR': 'Adults',
    'PG-13': 'Teens',
    'TV-G': 'Kids',
    'PG': 'Older Kids',
    'G': 'Kids',
    'UR': 'Adults',
    'NC-17': 'Adults'
}
data['target_age'] = data['rating'].replace(ratings_ages)

data['country_main'] = data['country'].apply(lambda x: x.split(",")[0])

movie_df = data[data['type'] == 'Movie']
tv_df = data[data['type'] == 'TV Show']


# pie chart the content on Netflix dataset has 30.9% TV shows and 69.1% Movies.
x = data['type'].value_counts().reset_index()
fig = px.pie(x, values='type', title='CONTENTS ON NETFLIX', names='index', color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textposition='inside', textinfo='percent+label', marker=dict(line=dict(color='white', width=1)))
fig.show()

# pie chart based on countries
country_df = data['country_main'].value_counts().reset_index()
country_df = country_df[country_df['country_main'] / country_df['country_main'].sum() > 0.01]
fig = px.pie(country_df, values='country_main', title= "BASIS OF COUNTRY's PRODUCTION", names='index', color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textposition='inside', textinfo='percent+label', marker=dict(line=dict(color='white', width=1)))
fig.show()

# content added with respect to the country_main
fig = px.histogram(data, x='country_main', title='content added with respect to the country_main', color_discrete_sequence=['indianred'])
fig.update_xaxes(categoryorder='total ascending')
fig.show()

# plot shows the percentage of movies added based upon the target age
def generate_age_df(df):
    new_df = df.groupby(['target_age']).agg({'show_id': 'count'}).reset_index()
    new_df = new_df[new_df['show_id'] != 0]
    new_df.columns = ['target_age', 'counts']
    new_df = new_df.sort_values('target_age')

    return new_df

movie_age_df = generate_age_df(movie_df)
fig = px.pie(labels = movie_age_df['target_age'], values = movie_age_df['counts'], names = movie_age_df['target_age'], title='movies added based upon the target age', width = 550, height = 550)

fig.update_traces(textposition = 'inside',textinfo = 'percent + label', hole = 0.75,marker = dict(colors = ['#3D0C02', '#800000'  , '#C11B17','#C0C0C0'],
                                line = dict(color = 'white', width = 2)))

fig.update_layout(annotations = [dict(text = 'Movies', x = 0.5, y = 0.5, font_size = 40, showarrow = False,font_color = 'black')],
                  showlegend = False)

fig.show()

# plot shows the percentage of TV series added based upon the target age.
tv_age_df = generate_age_df(tv_df)
fig = px.pie(labels = tv_age_df['target_age'], values = tv_age_df['counts'], names = tv_age_df['target_age'], title='TV series added based upon the target age', width = 550, height = 550)

fig.update_traces(textposition = 'inside',textinfo = 'percent + label',
                  hole = 0.75, marker = dict(colors = ['#3D0C02', '#800000'  , '#C11B17','#C0C0C0'], line = dict(color = 'white', width = 2)))

fig.update_layout(annotations = [dict(text = 'TV Series',x = 0.5, y = 0.5, font_size = 36, showarrow = False,
                                      font_color = 'black')], showlegend = False)

fig.show()

distplot is based upon the release_year of the movies/shows.
from scipy.stats import norm

sns.distplot(data.loc[data['release_year'] > 2000, 'release_year'],fit= norm, kde=False,
                   color='#827839')
plt.title('distplot is based upon the release_year of the movies/shows.',)
plt.show()
