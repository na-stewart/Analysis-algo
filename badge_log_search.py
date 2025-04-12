import random
from collections import deque, defaultdict
from datetime import datetime, timedelta


def has_excessive_swipes(swipe_times, k):
    swipe_times = sorted(datetime.strptime(t, "%H:%M:%S") for t in swipe_times)
    window = deque()
    max_window = []
    for time in swipe_times:
        print(f"Checking time: {time.strftime('%H:%M:%S')}")
        window.append(time)
        log(f"Window after adding time {time.strftime('%H:%M:%S')}: {[t.strftime('%H:%M:%S') for t in window]}")
        while (time - window[0]) > timedelta(hours=1):
            removed = window.popleft()
            log(f"Removing time {removed.strftime('%H:%M:%S')} as it is outside the 1-hour window", "bad")
        if len(window) > len(max_window):
            max_window = list(window)
            log(f"New max window: {[t.strftime('%H:%M:%S') for t in max_window]}", "good")
    log(f"Final max window: {[t.strftime("%H:%M:%S") for t in max_window]}")
    return (len(max_window) > k), [t.strftime("%H:%M:%S") for t in max_window]


def generate_random_time(base_hour=None):
    # Creates time string with random ints.
    if base_hour is not None:
        hour = base_hour
    else:
        hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return f"{hour:02}:{minute:02}:{second:02}"


def log(msg, level="info"):
    colors = {"info": "\033[34m", "good": "\033[92m", "bad": "\033[31m"}
    print(f"{colors[level]}{msg}\033[0m")


if __name__ == "__main__":
    badge_swipes_map = defaultdict(list)
    for _ in range(20):  # Generate users
        user_id = random.randint(0, 100)
        clustered_hour = random.randint(0, 23)
        for _ in range(30):  # Generate multiple swipes
            if random.random() < 0.2:
                timestamp = generate_random_time(clustered_hour)
            else:
                timestamp = generate_random_time()
            badge_swipes_map[user_id].append(timestamp)
    log("Good Afternoon. Author: Nicholas Stewart")
    log(f"Here are available user ids: {[swipe for swipe in badge_swipes_map.keys()]}")
    while True:
        print()
        user_id_index = int(input("Enter index of user ID to check for excessive swipe-ins in an hour (or -1 to quit): "))
        try:
            user_id = [swipe for swipe in badge_swipes_map.keys()][user_id_index]
        except IndexError:
            log("Incorrect input, please enter \"index\" of user ID.", "bad")
            continue
        if user_id_index == -1:
            log("Exiting...")
            break
        k = 7
        swipes = badge_swipes_map[user_id]
        status, swipes_in_hour = has_excessive_swipes(swipes, k)
        if status:
            log(f"User {user_id} has more than {k} swipes in a single hour.", "bad")
        else:
            log(f"User {user_id} does NOT exceed 7 swipes in any one-hour period.", "good")
        log(f"Swipe times within the most active hour window ({len(swipes_in_hour)} swipes).")
