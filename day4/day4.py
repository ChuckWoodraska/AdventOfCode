import re
from operator import itemgetter
import pprint
from datetime import datetime

log_data = []
guard_minute_sleep = {}


def load_log(log):
    for line in log:
        line_search = re.search(r'\[(\d+\-\d+\-\d+\s\d+:\d+)\]\s(Guard #|falls|wakes)(\d*)', line)
        log_data.append((line_search.group(1), line_search.group(2), line_search.group(3),))


with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    load_log(data)
    log_data = sorted(log_data, key=itemgetter(0))
    pprint.pprint(log_data)
    current_id = None
    start_time = None
    for log in log_data:
        if 'Guard' in log[1]:
            current_id = log[2]
        elif 'falls' in log[1]:
            start_time = datetime.strptime(log[0], '%Y-%m-%d %H:%M')
        else:
            if current_id not in guard_minute_sleep:
                guard_minute_sleep[current_id] = {'minute_counts': {}, 'total_minutes': 0}
            end_time = datetime.strptime(log[0], '%Y-%m-%d %H:%M')
            delta = end_time - start_time
            smin = start_time.minute
            guard_minute_sleep[current_id]['total_minutes'] += int(delta.seconds / 60)
            sleep_range = range(smin, smin + int(delta.seconds / 60))
            for x in sleep_range:
                if x in guard_minute_sleep[current_id]['minute_counts']:
                    guard_minute_sleep[current_id]['minute_counts'][x] += 1
                else:
                    guard_minute_sleep[current_id]['minute_counts'][x] = 1
    # PART 1
    top_sleeper = sorted(guard_minute_sleep, key=lambda x: guard_minute_sleep[x]['total_minutes'], reverse=True)[0]
    # print(top_sleeper)
    top_minute = max(guard_minute_sleep[top_sleeper]['minute_counts'].items(), key=itemgetter(1))[0]
    # print(top_minute)
    print(int(top_sleeper) * int(top_minute))
    # PART 2
    max_dict = {'id': 0, 'sleep': 0, 'max': 0}
    for k in guard_minute_sleep.keys():
        minute_max = max(guard_minute_sleep[k]['minute_counts'].items(), key=itemgetter(1))
        if max_dict.get('max') < minute_max[1]:
            max_dict['id'] = k
            max_dict['sleep'] = minute_max[0]
            max_dict['max'] = minute_max[1]
    print(int(max_dict.get('sleep'))*int(max_dict.get('id')))
