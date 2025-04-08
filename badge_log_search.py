import random
from collections import deque
from datetime import datetime, timedelta


def has_excessive_swipes(swipe_times, k):
    swipe_times = sorted([datetime.strptime(t, "%H:%M:%S") for t in swipe_times])
    window = deque()
    for time in swipe_times:
        window.append(time)
        while (time - window[0]) > timedelta(hours=1):
            window.popleft()
        if len(window) > k:
            return True, [t.strftime("%H:%M:%S") for t in list(window)]
    return False, []


if __name__ == "__main__":
    badge_swipes_map = {}

    # FIX GENERATION SO THAT MULTIPLE SWIPES PER ONE USER ID. idk that this generation is lmfao.

    for _ in range(100):  # Generates badge swipes map.
        random_time = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}"
        badge_swipes_map[random.randint(0, 100)] = random_time

    print("Good Afternoon. == Author: Nicholas Stewart")

    print(f"Here are available user ids: {[swipe for swipe in badge_swipes_map.keys()]}")
    while True:
        user_id = int(input("Enter user ID to check for excessive swipe-ins in an hour (or -1 to quit): "))
        if user_id == -1:
            print("Exiting...")
            break
        if user_id not in badge_swipes_map:
            print("User ID not found. Try again.")
            continue
        swipes = badge_swipes_map[user_id]
        status, swipes_in_hour = has_excessive_swipes(badge_swipes_map.values(), 7)
        if status:
            print(f"User {user_id} has more than 7 swipes in a single hour.")
            print(f"Swipe times within the hour window: {swipes_in_hour}")
        else:
            print(f"User {user_id} does NOT exceed 3 swipes in any one-hour period.")
