import math

menu = """Investment - to calculate the amount of interest you'll earn on your investment
Bond - to calculate the amount you'll have to pay on a home loan"""

# Create a menu the user can choose from and display it
print(menu)

# Ask user to input either investment or bond
selection = input("""Enter either 'Investment' or 'Bond'
from the menu above to proceed: """).lower()

# Ask the user to input the variables if they selected investment
if selection == 'investment':
    P = float(input("Please enter the amount of money you are depositing £: "))
    r = float(input("Please enter the interest rate: "))/100
    t = float(input("Please enter how many years do you wish to invest for: "))

# Ask user if they want to choose compound or simple interest
    interest = input("""Please enter if you would
like simple or compound interest: """).lower()

# Calculate and display the value of simple interest
    if interest == "simple":
        simple_interest = P*(1 + r*t)
        print("The total amount is" + "£", simple_interest)

# Calculate and the display the value of compound interest
    elif interest == "compound":
        compund_interest = P * math.pow((1+r), t)
        print("The total amount you will save is " + "£", compund_interest)
   
   # There is an error message if compound or simple interest isn't chosen
    else:
        print("There seems to be an error, please try again.")

# If user selects "Bond" from the menu, ask user to input 3 variable
elif selection == "bond":
    P = float(input("Please enter the value of the house at present: "))
    i = float(input("Please enter the interest rate: "))/100
    n = float(input("""Please enter the amount of months
you plan to repay the bond over: """))
    
    # Calculate and display the bond value
    repayment = (i * P)/(1-(1+i)**(-n))
    print("Your repayment amount per month is: " + "£", repayment)

# If the user doesn't selected anything recognised from the menu, an error message is displayed.
else: 
    print("There appears to be an error, please try again.")