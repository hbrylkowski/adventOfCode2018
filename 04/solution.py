import re
from functools import reduce

with open('input') as f:
    raw_data = f.read().splitlines()

timeline = sorted(raw_data)

guards = {}

regex_guard_id = re.compile('#\d+')
regex_minute = re.compile(' \d+\:(\d+)')

for event in timeline:
    event_time = event[1:17]
    event_date = event[1:11]
    if event[-5:] == "shift":
        current_guard_id = regex_guard_id.search(event).group(0)[1:]
        if current_guard_id not in guards:
            guards[current_guard_id] = [[] for _ in range(60)]

    elif event[-6:] == 'asleep':
        minute_asleep = int(event_time[-2:])

    elif event[-2:] == 'up':
        minute_up = int(event_time[-2:])
        for m in range(minute_asleep, minute_up):
            guards[current_guard_id][m].append(event_date)

biggest_sleeper = max(guards, key=lambda g: len(reduce(list.__add__, guards[g], [])))
longest_minute = guards[biggest_sleeper].index(max(guards[biggest_sleeper], key=lambda g: len(g)))
print(int(biggest_sleeper) * longest_minute)

most_frequent_sleeper = max(guards, key=lambda g: len(max(guards[g], key=lambda w: len(w))))
most_frequent_minute = guards[most_frequent_sleeper].index(max(guards[most_frequent_sleeper], key=lambda g: len(g)))
print(int(most_frequent_sleeper) * most_frequent_minute)
