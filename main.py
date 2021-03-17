import mindwave
import time
import json
import os

sampling_rate = 100
time_delta = 1 / sampling_rate
recording_time = 50

total_samples = recording_time * sampling_rate


print("Connecting...")
headset = mindwave.Headset("/dev/tty.MindWaveMobile-SerialPo")
time.sleep(3)  # takes a while to establish connection on my device
print("Connected!")

# make sure connection is good
while headset.poor_signal > 5:
    print("Poor connection or signal, try readjusting headset")
    print(headset.attention)
    time.sleep(1)


name = input("Enter name:  ")

while True:
    print("Going to collect 40 seconds of data after you enter your trial type")
    clip_data = input("clip name, then vr (ex dab T):::")
    clip_name = clip_data.split(" ")[0]
    clip_vr = clip_data.split(" ")[1]

    attention_data = []
    eeg_data = []

    print("collecting")

    # capping out songs at 2 mins for training seems ok (128 * 120 = 15360 samples per trial)
    for i in range(total_samples):

        while headset.poor_signal > 5:
            # shouldn't happen
            print("Poor connection or signal, try readjusting headset")
            print("and probably restart trial")
            time.sleep(1)

        attention_data.append(headset.attention)
        eeg_data.append(headset.raw_value)

        time.sleep(time_delta)

    print("finished collecting samples, saving")

    saved_data = {"attention": attention_data, "eeg": eeg_data}

    filename = f"data_{name}_clip_{clip_name}_vr_{clip_vr}.json"

    with open(os.path.join("data", filename), "w") as f:
        json.dump(saved_data, f)

    print("Wrote data, you can safely quit")
    time.sleep(5)
