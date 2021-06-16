import pandas as pd
movie = pd.read_csv('movie_bd_v5.csv')

print(movie.info())

print('самый дорогой фильм')
budget = movie[movie.budget == movie.budget.max()]
print(budget.head(1))

print('самый длинный фильм')
runtimeMax = movie[movie.runtime == movie.runtime.max()]
print(runtimeMax.head(1))

print('Самый короткий фильм')
runtimeMin = movie[movie.runtime == movie.runtime.min()]
print(runtimeMin.head(1))

print('средняя длительность')
print(movie.runtime.mean())

print('медиана')
print(movie.runtime.median())

print('самый прибыльный фильм')
movie['profite'] = movie['revenue'] - movie['budget']
maxProfit = movie[movie.profite == movie.profite.max()]
print(maxProfit)

print('самый убыточный фильм')
movie['profite'] = movie['revenue'] - movie['budget']
minProfit = movie[movie.profite == movie.profite.min()]
print(minProfit)

print('у скольких фильмов сборы больше бюджета')
movie['profite'] = movie['revenue'] - movie['budget']
profitFilms = movie[movie.revenue > movie.budget]
print(len(profitFilms))

print('самый кассовый фильм 2008')
movie['profite'] = movie['revenue'] - movie['budget']
profit2008 = movie[movie.release_year == 2008]
print(profit2008[profit2008.revenue == profit2008.revenue.max()])

print('самый убыточный фильм с 2012 по 2014')
movie['profite'] = movie['revenue'] - movie['budget']
nonProfiteFilms = movie[movie.release_year.between(2012, 2014, False)]
print(nonProfiteFilms[nonProfiteFilms.profite == nonProfiteFilms.profite.min()])

print('Какого жанра фильмов больше всего?')
print(movie.genres.value_counts().head(1))

print('Какой жанр чаще всего становится прибыльным')
print(movie[movie.revenue > movie.budget].genres.value_counts())

print('У какого режиссера самые большие суммарные кассовые сборы?')
bestDirecotr = movie.groupby(['director']).sum();
print(bestDirecotr[bestDirecotr.revenue==bestDirecotr.revenue.max()])

print('Какой режиссер снял больше всего фильмов в стиле Action?')
movie = pd.read_csv('movie_bd_v5.csv')
movie = movie[movie['genres'] == 'Action']
movie = movie['director'].apply(lambda s: str(s).split('|'))
movie = movie.explode('director')
print(movie.value_counts())


print('Самый убыточный фильм от Парамоунт')
movie = pd.read_csv('movie_bd_v5.csv')
movie['profite'] = movie['revenue'] - movie['budget']
movie = movie[(movie.production_companies == 'Paramount Pictures') & (movie.budget > movie.revenue)]
print(movie[movie.revenue == movie.revenue.min()])
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(movie.head()
#
#     )

print('какой год стал самым успешным')
movie = pd.read_csv('movie_bd_v5.csv')
movie = movie.groupby(['release_year'])['revenue'].sum()
print(movie)
print(' Какой самый прибыльный год для студии Warner Bros')
movie = pd.read_csv('movie_bd_v5.csv')
movie['profite'] = movie['revenue'] - movie['budget']
warner_df = movie[movie['production_companies'].str.contains('Warner Bros')]
warner_df = warner_df.groupby(['release_year'])['profite'].sum().sort_values(ascending=False)
print(warner_df)