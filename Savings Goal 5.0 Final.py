# Savings Goal 5.0, Final 4th Practice Problem with additions
# define a function for annual savings calculation
def savings_goal(salary):
    savings = salary * 0.2
    return savings


# set input field for annual salary
print("You should be saving!")
print("A good target is 20%.")
print(" ")
salary_input = float(input("What is your annual salary? "))
savings = savings_goal(salary_input)
print("Your annual savings goal is $" +str(savings))    #output

# define a function for a percheck savings amount
def percheck_target(savings, monthly):
    percheck = savings / (monthly * 12)
    return percheck


# set input field for number of pay periods per month
print(" ")  # is there a better way to add a space?
monthly_input = float(input("How many times do you get paid a month? "))
percheck = percheck_target(savings, monthly_input)
print("You should save: $" + str(percheck) + " per paycheck")   #output

print(" ")  # is there a better way to add a space?
# TRUTH BOMB
def wealth_steal(savings):
    steal = savings - (savings * (1-0.06))
    return steal


steal = wealth_steal(savings)
conditional_statement = input("Do you want to save in Bitcoin or Fiat? ")

if conditional_statement == "Fiat":
    print("You will lose: $" + str(steal) + " this year due to inflation.")
    print("Maybe you should save in bitcoin.")
    print(" ")
    conditional_statement = input("Do you want to save in Bitcoin or Fiat? ")
elif conditional_statement == "fiat":
    print("You will lose: $" + str(steal) + " this year due to inflation.")
    print("Maybe you should save in bitcoin.")
    print(" ")
    conditional_statement = input("Do you want to save in Bitcoin or Fiat? ")

if conditional_statement == "Bitcoin":
    print("You will gain: $" + str(steal) + " this year over inflation by saving in Bitcoin.")
    print("Fiat is a shitcoin.")
elif conditional_statement == "bitcoin":
    print("You will gain: $" + str(steal) + " this year over inflation by saving in Bitcoin.")
    print("Fiat is a shitcoin.")
else:
        print("What are you stupid.")





















