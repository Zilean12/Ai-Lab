x = ['F', 'W', 'G', 'C']  # Initial state: M = Farmer, W = Wolf, G = Goat, C = Cabbage
y = []  # Right side of the river initially empty

print("Before Process")
print("Element in the Left Side Bank  ", x)
print("Element in the Right Side Bank  ", y)

while True:  # Main loop for the river crossing process
    # Prompting user to select an item to move
    print(x[1], " ", x[2], " ", x[3], "Select any one from the list")
    i = input("Enter the item: ")
    i = i.upper()  # Convert input to uppercase for case-insensitivity
    
    # Conditions for ensuring safety during the crossing
    if x[1] == i and x[2] == 'G' and x[3] == 'C':
        print("Goat will eat Cabbage")
        break
    elif x[2] == i and x[3] != 'C':
        y.append(x[2])
        if len(y) == 2 and y[0] == 'G':
            x[2] = y[0]
            y[0] = y[1]
            y.pop()
    elif x[1] == i and x[2] == 'G':
        y.append(x[1])
        x[1] = x[2]
        x[2] = ''
    elif x[1] == i and x[2] == 'C':
        y.append(x[1])
        x[1] = x[2]
        x[2] = ''
        if len(y) == 2 and y[0] == 'G':
            x[2] = y[0]
            y[0] = y[1]
            y.pop()
    elif x[1] == i and x[2] != 'C' and x[2] != 'G':
        y.append(x[1])
        y.append('F')
        x[1] = ''
        x = []
        print("Goal is Reached")
        break

    # if user select the cabbage then possible out come will be  
    elif x[2] == i and x[3] == 'C':
        y.append(x[2])
        x[2] = x[3]
        x[3] = ''
    elif x[3] == i:
        print("Wolf will Eat Goat")
        break

# Output after each process
print("After Process")
print("Element in the Left Side Bank  ", x)
print("Element in the Right Side Bank  ", y)