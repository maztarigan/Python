#define new function
def print_name(name): #name is required arguments / mandatory
    print(name.center(80,"-"))
    print("-"*80) 

#Call print_name function
print_name("Mazmur")

#many required arguments
def print_name2(name, age, email): #name,age,email is required arguments / mandatory
    print(name.center(80,"-"))
    print(age.center(80," "))
    print(email.center(80," "))
    print("-"*80) 

#Call print_name2 function
# print_name2("Mazmur","17","dev.mazmur@gmail.com")

#using keyword arguments
print_name2(name="Mazmur",email="dev.mazmur@gmail.com", age="17")

#default arguments
def print_name3(name, age, email="dev.mazmur@gmail.com"): #email is default arguments, must be insert in last required arguments
    print(name.center(80,"-"))
    print(age.center(80," "))
    print(email.center(80," "))
    print("-"*80) 

#call the default argument function 
#default argument not mandatory
print_name3(name="Mazmur",age="17")
