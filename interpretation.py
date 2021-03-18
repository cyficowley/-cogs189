#%%
import json
import matplotlib.pyplot as plt
import numpy as np
import os

# %%


files = [f for f in os.listdir("data")]


def is_vr(name):
    return name.split("_")[-1].startswith("T")


def get_person(name):
    return name.split("_")[1]


def get_clip_num(name):
    return name.split("_")[3]


data = {
    file_name: json.load(open(os.path.join("data", file_name))) for file_name in files
}


#%%

# Stats To Get

# Overall attention levels between VR and non VR

attention_vr = []
attention_non_vr = []

for name, value_dic in data.items():
    if is_vr(name):
        attention_vr.append(np.median(value_dic["attention"]))
    else:
        attention_non_vr.append(np.median(value_dic["attention"]))


print(attention_vr)
print(attention_non_vr)

fig, ax = plt.subplots()
ax.set_title("attention levels")

ax.bar(
    ["vr", "non vr"],
    [np.median(attention_vr), np.median(attention_non_vr)],
)

#%%
# Graphs of average/median attention for each clip

clip = [0] * 4

for name, value_dic in data.items():
    if is_vr(name):
        attention_vr.append(np.median(value_dic["attention"]))
    else:
        attention_non_vr.append(np.median(value_dic["attention"]))


print(attention_vr)
print(attention_non_vr)

plt.bar(["vr", "non vr"], [np.median(attention_vr), np.median(attention_non_vr)])


#%%


# Graphs of average/median attention for each clip split by vr/non vr

# Difference between VR and non VR per person

# %%
