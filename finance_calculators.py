import math

# user should sleect option for calculation

while True:
    user_options = "\nInvestment - to calculate the amount of interest you'll earn on your investment\n"
    user_options += "Bond - to calculate the amount you'll have to pay on a home loan\n"
    user_options += "\nEnter either 'investment' or 'bond' from the menu above to proceed:"

    user_select = input(user_options)

    # make the chracters of the input lowercase so the input is not case sensitive 

    user_select = user_select.lower()

    # if user selects investments

    
    if user_select == "investment":
        
        


    # make sure the user input for deposit time and rate cannot be less than 0

        while True:
            deposit = int(input("please enter deposit amount:"))
            if deposit < 0:
                print("cant be less than 0")
            else:
                break

        while True:
            time = int(input("please input time in years:")) 
            if time < 0:
                print("cant be less than 0")  
            else:
                break

        while True:
            rate = int(input("please enter interest rate:"))   
            if rate < 0:
                print ("cant be les than 0")    
            else:
                break
            
            # user needs to pick either simple or compound interest

        while True:
            intrest_type = "would you like 'simple' or 'compound' interest\n"
            intrest_type += "please enter your choice:"

            intrest = input(intrest_type)

            if intrest == "simple":
                
                # simple formula 
                
                total = deposit * (1 + (rate / 100) * time)

                print(f"Balance after {time} years is : £{total:.2f}\n") 
                break

            elif intrest == "compound":
                
                # compound formula 

                total = deposit * math.pow(1+(rate/100),time)

                print(f"Balance after {time} years is : £{total:.2f}\n")
                break
                
            
        break    
            # if the user select bond
         

    elif user_select == "bond":
        house_value = int(input("what is the value of house:"))
        int_rate = int(input("what is the interest rate:"))
        months = int(input("how many months:"))

        monthly_int_rate = (int_rate / 100) / 12 
        
        # bond formula

        repayment = (monthly_int_rate * house_value) / (1 - (1 + monthly_int_rate)**(-months))


        print(f"You will have to repay £{repayment:.2f} every month\n")
        break
        

    else:
        print("invalid")

        

    
    