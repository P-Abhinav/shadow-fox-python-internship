"""ShadowFox Python Internship - Task 1: For Loop"""

import random

# 1. Roll a six-sided die 20 times and calculate requested statistics.
rolls = [random.randint(1, 6) for _ in range(20)]

six_count = rolls.count(6)
one_count = rolls.count(1)
two_sixes_in_row = sum(
    rolls[i] == 6 and rolls[i - 1] == 6
    for i in range(1, len(rolls))
)

print("Die rolls:", rolls)
print("Times rolled a 6:", six_count)
print("Times rolled a 1:", one_count)
print("Times two 6s occurred in a row:", two_sixes_in_row)

# 2. Workout: 100 jumping jacks, 10 at a time.
completed = 0

for _ in range(10):
    completed += 10
    remaining = 100 - completed

    if remaining == 0:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").strip().lower()
    if tired in {"yes", "y"}:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in {"yes", "y"}:
            print(f"You completed a total of {completed} jumping jacks.")
            break
    else:
        print(f"{remaining} jumping jacks are remaining.")
