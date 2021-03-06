import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import networkx as nx

df = pd.read_csv('/home/aliiz/Desktop/recommender/goodbooks-10k/ratings.csv')

books_size = 100
users_size = 100


def make_subset_of_dataset():
    subset_of_df = df.loc[df['book_id'] < books_size]
    subset_of_df = subset_of_df.loc[subset_of_df['user_id'] < users_size]
    return subset_of_df


def draw_dataset(subset_of_df):
    fig, ax = plt.subplots(figsize=(15, 7))
    subset_of_df.groupby(['book_id', 'rating']).count().sort_values(['user_id'], ascending=False)['user_id'].unstack().plot(ax=ax)
    plt.show()


def make_adjacency_matrix(subset_of_df):

    users_id_size = subset_of_df.user_id.nunique()
    users = subset_of_df.user_id.unique()

    users_dict = {v: index for index, v in np.ndenumerate(users)}

    matrix = np.zeros((users_id_size + 5 * books_size, users_id_size + 5 * books_size))

    start_time = datetime.now()

    for index, row in subset_of_df.iterrows():
        matrix[users_dict[row['user_id']], users_id_size + row['book_id'] + (row['rating'] - 1) * books_size] = 1

    time_elapsed = datetime.now() - start_time

    print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

    return matrix


subset = make_subset_of_dataset()
matrix = make_adjacency_matrix(subset)

G = nx.from_numpy_matrix(matrix)

preds = nx.resource_allocation_index(G)

predicted_link = []
for u, v, p in preds:
    if p != 0:
        predicted_link.append(p)
        # print('(%d, %d) -> %.8f' % (u, v, p))

print(predicted_link)




















