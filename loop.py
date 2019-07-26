#loop using while
x =10
while x < 100:
    print(x)
    x += 1
    
    # break loop
    if x ==13:
       break

print("done")

#loop using for

# Prints out the numbers 0,1,2,3
for x in range(4):
    print(x)
print("done")

# Prints out 3,4
for x in range(3, 5):
    print(x)
print("done")

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)