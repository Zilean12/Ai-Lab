#library
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt


# Independent variable
independent_variable = "Height (cm)"

# Range 
min_range = 0
max_range = 300

# granularity variable (step size)
granularity = 100

fuzzy_sets = ["Very Short", "Short", "Medium", "Tall", "Very Tall"]

def fuzzy_set(func):
    def wrapper(x):
        return func(x)
    return wrapper

# very short 
def very_short(x):
    return max(0, min(1, (50 - x) / 50))

#short
def short(x):
    return max(0, min(1, (x - 50) / 50, (150 - x) / 50))

#medium
def medium(x):
    return max(0, min(1, (x - 100) / 50, (200 - x) / 50))

#tall
def tall(x):
    return max(0, min(1, (x - 150) / 50, (250 - x) / 50))

#very tall
def very_tall(x):
    return max(0, min(1, (x - 200) / 50))

# union function
def union(set1, set2, x):
    return max(set1(x), set2(x))

# intersection function
def intersection(set1, set2, x):
    return min(set1(x), set2(x))

# complement function
def complement(set1, x):
    return 1 - set1(x)

x_values = np.arange(min_range, max_range + 1, granularity)

membership_values = {}
for fuzzy_set in fuzzy_sets:
    membership_values[fuzzy_set] = [globals()[fuzzy_set.replace(" ", "_").lower()](x) for x in x_values]
    
# Graph (using matplotlib library)
# membership of fuzzy set

plt.figure(figsize=(10, 6))
for fuzzy_set in fuzzy_sets:
    plt.plot(x_values, membership_values[fuzzy_set], label=fuzzy_set)
plt.title("Membership Functions of Fuzzy Sets")
plt.xlabel(independent_variable)
plt.ylabel("Membership Value")
plt.legend()
plt.grid(True)
plt.show()

# union, intersection, complement,
plt.figure(figsize=(10, 6))
plt.plot(x_values, membership_values["Very Short"], label="Very Short")
plt.plot(x_values, membership_values["Short"], label="Short")
plt.plot(x_values, [union(very_short, short, x) for x in x_values], label="Union (Very Short, Short)")
plt.plot(x_values, [intersection(very_short, short, x) for x in x_values], label="Intersection (Very Short, Short)")
plt.plot(x_values, [complement(very_short, x) for x in x_values], label="Complement (Very Short)")
plt.title("Union, Intersection, and Complement of Fuzzy Sets (Very Short, Short)")
plt.xlabel(independent_variable)
plt.ylabel("Membership Value")
plt.legend()
plt.grid(True)
plt.show()
