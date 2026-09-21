import time
import random

reaction_times = []
print("REACTION TIME GAME")

for attempt in range(1, 6):
    input(f"\nPress Enter when you're ready for attempt {attempt}...")

    timer_length = random.uniform(2, 5)

    start_time = time.monotonic()
    while True:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time

        if elapsed_time >= timer_length:
            break

    print("GO!")
    go_start_time = time.monotonic()
    input()
    go_end_time = time.monotonic()

    reaction_time = go_end_time - go_start_time
    reaction_times.append(reaction_time)

    
    print(f"Reaction time: {reaction_time:.3f} seconds")


fastest_time = min(reaction_times)
print(f"\nFastest Reaction Time: {fastest_time:.3f} seconds")
