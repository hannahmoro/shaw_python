#create the funciton cheese and crackers that prints messages
def cheese_and_crackers(cheese_count, boxes_of_crakers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crakers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) #uses the function with 20 cheeses and 30 boxes of crackers

print("OR, we can use variables from our script:") #message, then sets variables
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #uses function with set variables

print("We can even do math inside, too:")
cheese_and_crackers(10 + 20, 5 + 6) #uses function with values added together

print("And we can combine the two, variables and math:") #message then uses function with vars plus values
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def my_first_function(name, number):
    print(f"This is {name}'s first function!")
    print(f"It is the first function of at least {number}...")
    print(f"In the future, this function will seem SO simple to {name}")

my_first_function("Hannah", 100+10)

me = "Hannah M"
n_lifetime_functions = 10200

my_first_function(me, n_lifetime_functions)