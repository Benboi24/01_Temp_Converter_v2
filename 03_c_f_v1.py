# quick component to convert to degrees C to F.
# Functions takes in value, does conversion and puts answer into a list


def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit


# Main Routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} F".format(item, answer)
    converted.append(ans_statement)

print(converted)