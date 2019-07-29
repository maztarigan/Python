#variable arguments
def print_name(name, age, email, *newvarible): #newvariable is variable argument, flexible variable
    print(name.center(80,"-"))
    print(age.center(80," "))
    print(email.center(80," "))
    for arg in newvarible:
        print(arg)
    print("-"*80) 
    print("\n")

print_name("Mazmur","17","dev.mazmur@gmail.com") #call funciton without variable arguments
print_name("Mazmur","17","dev.mazmur@gmail.com",20) #call funciton with variable arguments
print_name("Mazmur","17","dev.mazmur@gmail.com",20,30,40) #call funciton with variable arguments