commit_times = [(66,15), (8,45), (12, 45), (27, 132)]
for time in commit_times:
    hour = time[0]
    minutes = time[1]
    if not (0 <= hour <= 24 and 0 <= minutes <= 59):
        continue
    print("Someone commited at {h}:{m}".format(h=hour, m=minutes))
