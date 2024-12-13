import math

def round_if_float(value):
    if isinstance(value, float):
        return round(value, 3)
    return value

def sine(angle):
    return round_if_float(math.sin(math.radians(angle)))

value_1 = 2
result = value_1

result = sine(result if int(abs(result)) not in [0, 1] else value_1)
print(result)
