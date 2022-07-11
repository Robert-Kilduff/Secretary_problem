import numpy as np
import names as ns
import random
import pandas as pd


def best_of_three():
    lst = list(np.arange(1,101))
    random.shuffle(lst)
    apps = []
    for i in range(0, 100):
        apps.append(ns.get_full_name())
    df = pd.DataFrame({"Name": apps, "Rank": lst, "Known Rating": [None]*100})
    df2 = df[["Rank"]].copy()
    df = df.assign(Rank_Compare=(df2 < df2.cummin().shift()).all(1).astype(int))
    winner = df[df["Rank_Compare"].cumsum() == 3]
    winner = winner[winner["Rank_Compare"] == 1]
    return winner

