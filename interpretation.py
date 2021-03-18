#%%
import json
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.signal import savgol_filter

# %%


files = [f for f in os.listdir("data")]


def is_vr(name):
    return name.split("_")[-1].startswith("T")


def get_person(name):
    return name.split("_")[1]


def get_clip_num(name):
    return int(name.split("_")[3])


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
ax.set_title("median attention levels")

ax.bar(
    ["vr", "non vr"],
    [np.median(attention_vr), np.median(attention_non_vr)],
)

#%%
# Graphs of median attention for each clip

clip = [[], [], [], []]

for name, value_dic in data.items():
    clip[get_clip_num(name)].append(np.median(value_dic["attention"]))

fig, ax = plt.subplots()
ax.set_title("median attention per clip")
ax.bar(["CLIP {}".format(i + 1) for i in range(4)], [np.median(each) for each in clip])
#%%
# Graphs of median attention per time level for each clip
clip = [[], [], [], []]

for name, value_dic in data.items():
    clip[get_clip_num(name)].append((value_dic["attention"]))


for i, each in enumerate(clip):
    clip[i] = np.median(np.array(each), axis=0)


plt.plot(clip[0])
plt.plot(clip[1])
plt.plot(clip[2])
plt.plot(clip[3])


#%%
# Smoothed graphs of median attention per time level for each clip
for each in clip:
    plt.plot(savgol_filter(each, 301, 3))

#%%
clip = [[], [], [], []]

for name, value_dic in data.items():
    clip[get_clip_num(name)].append((value_dic["attention"]))


for i, each in enumerate(clip):
    clip[i] = np.std(np.array(each), axis=0)

# Smoothed graphs of standard deviation over attention for each clip.

for each in clip:
    plt.plot(savgol_filter(each, 301, 3))


#%%
# Graphs of average/median attention for each clip split by vr/non vr

# VR
clip = [[], [], [], []]

for name, value_dic in data.items():
    if is_vr(name):
        clip[get_clip_num(name)].append((value_dic["attention"]))

for i, each in enumerate(clip):
    clip[i] = np.std(np.array(each), axis=0)

for each in clip:
    plt.plot(savgol_filter(each, 301, 3))

#%%

# Non VR

clip = [[], [], [], []]

for name, value_dic in data.items():
    if not is_vr(name):
        clip[get_clip_num(name)].append((value_dic["attention"]))

for i, each in enumerate(clip):
    clip[i] = np.std(np.array(each), axis=0)

for each in clip:
    plt.plot(savgol_filter(each, 301, 3))


#%%


# Difference between VR and non VR per person


people_to_look_at = ["cyrus", "Kylie", "Mal", "Markus", "Vanessa", "Victoria"]

fig, axs = plt.subplots(2, 3)

for i, person in enumerate(people_to_look_at):
    attention_vr = []
    attention_non_vr = []

    for name, value_dic in data.items():
        if get_person(name) == person:
            if is_vr(name):
                attention_vr.append(np.median(value_dic["attention"]))
            else:
                attention_non_vr.append(np.median(value_dic["attention"]))

    axs[i // 3, i % 3].bar(
        ["vr", "non vr"],
        [np.median(attention_vr), np.median(attention_non_vr)],
    )

    axs[i // 3, i % 3].set_title("{}".format(person))

# %%
