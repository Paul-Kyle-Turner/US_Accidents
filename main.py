import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

from header import HEADER
from tmc import TMC_CODES


def regex_replacer(data):
    return "jklsanfljksdnflk"


def gather_data(file="data/US_Accidents_May19.csv"):
    with open(file, 'r+') as csv_file:
        data = pd.read_csv(csv_file, sep=',')
    return data.columns.values, data


def gen_severity_bar_chart(data):
    X, y = np.unique(data[:, 3], return_counts=True)

    plt.bar(X.tolist(), y.tolist())
    plt.show()


def gen_severity_log_bar_chart(data):
    X, y = np.unique(data[:, 3], return_counts=True)

    fig, ax = plt.subplots()
    ax.bar(X.tolist(), y.tolist())
    ax.set_yscale('log')

    plt.show()


if __name__ == '__main__':
    # Gather needed data and headers
    # headers, data = gather_data()
    # data.to_pickle('US_Accidents_May19.pickle')

    data = pd.read_pickle('data/US_Accidents_May19.pickle')

    description = data['Description'].tolist()
    print(description)

    # severity = data.loc[:, "Severity"]

    # y_co = TSNE().fit_transform(data, severity)

    # plt.scatter(y_co[0], y_co[1])
    # plt.show()



