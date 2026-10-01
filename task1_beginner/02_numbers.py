"""ShadowFox Python Internship - Task 1: Numbers"""

# 1. format(145, 'o') returns the octal representation of 145.
def format_number(number, representation):
    return format(number, representation)

result = format_number(145, "o")
print("1. Formatted result:", result)
print("   Representation: octal")

# 2. Circular pond.
radius = 84
pi = 3.14
area = pi * radius ** 2
water_per_square_meter = 1.4
water_liters = area * water_per_square_meter

print("2. Pond area:", area, "square meters")
print("   Water in pond:", int(water_liters), "liters")

# 3. Speed in meters per second.
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds
print("3. Speed:", int(speed), "m/s")
