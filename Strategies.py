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
    winner = winner.iat[0,1]
    return winner

def best_of_two():
    lst = list(np.arange(1,101))
    random.shuffle(lst)
    apps = []
    for i in range(0, 100):
        apps.append(ns.get_full_name())
    df = pd.DataFrame({"Name": apps, "Rank": lst, "Known Rating": [None]*100})
    df2 = df[["Rank"]].copy()
    df = df.assign(Rank_Compare=(df2 < df2.cummin().shift()).all(1).astype(int))
    winner = df[df["Rank_Compare"].cumsum() == 2]
    winner = winner[winner["Rank_Compare"] == 1]
    winner = winner.iat[0,1]
    return winner

def look_leap(stop, list_len):
    lst = list(np.arange(1,list_len))
    random.shuffle(lst)
    stop_nr = (len(lst)/100) * stop
    wait_group = lst[0:stop_nr]
    pick_group = lst[stop_nr:]
    for i in pick_group:
        if i < min(wait_group) and i <= min(pick_group[0:pick_group.index(i)]):
            return i
        else:
            pass
    return 100

