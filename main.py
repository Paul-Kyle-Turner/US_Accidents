import numpy as np
import pandas as pd
import re

import matplotlib.pyplot as plt

from sklearn.manifold import TSNE

# Simple regex to change the multiple white space issue
def regex_replacer(description):
    reg_description = []
    for desc in data:
        reg_description.append(re.sub(desc, r'\s+', ' '))
    return reg_description


def gather_data(file="US_Accidents_May19.csv"):
    with open(file, 'r+') as csv_file:
        data = pd.read_csv(csv_file, sep=',')
    return data.columns.values, data


if __name__ == '__main__':
    # Gather needed data and headers
    # headers, data = gather_data()
    # data.to_pickle('US_Accidents_May19.pickle')

    data = pd.read_pickle('US_Accidents_May19.pickle')

    description = data['Description'].tolist()
    print(description)

    # severity = data.loc[:, "Severity"]

    # y_co = TSNE().fit_transform(data, severity)

    # plt.scatter(y_co[0], y_co[1])
    # plt.show()



