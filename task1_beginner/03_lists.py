"""ShadowFox Python Internship - Task 1: Lists"""

justice_league = [
    "Superman", "Batman", "Wonder Woman",
    "Flash", "Aquaman", "Green Lantern"
]

# 1. Number of members.
print("1. Number of members:", len(justice_league))
print(justice_league)

# 2. Add Batgirl and Nightwing.
justice_league.extend(["Batgirl", "Nightwing"])
print("\n2. After adding Batgirl and Nightwing:")
print(justice_league)

# 3. Move Wonder Woman to the beginning.
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. Wonder Woman moved to the beginning:")
print(justice_league)

# 4. Move Green Lantern between Aquaman and Flash.
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("\n4. Green Lantern moved between Aquaman and Flash:")
print(justice_league)

# 5. Replace with the new team.
justice_league = [
    "Cyborg", "Shazam", "Hawkgirl",
    "Martian Manhunter", "Green Arrow"
]
print("\n5. New Justice League:")
print(justice_league)

# 6. Sort alphabetically; index 0 becomes leader.
justice_league.sort()
print("\n6. Alphabetically sorted:")
print(justice_league)
print("New leader:", justice_league[0])
