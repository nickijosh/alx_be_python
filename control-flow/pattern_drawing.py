# prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

#initialize row counter
row = 0

# draw the patter
while row < size:
    for col in range(size):
        print("*", end="")
    print() # move to the next line after each row
    row += 1