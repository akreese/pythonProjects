#!/bin/python3


#
# Complete the 'sales_summary' function below.
#
"""
    Code I am pleased with:
I am pleased with my decision to use a nested dictionary for this coding challenge. It ended up being the perfect way to store the data we want to output. Using a nested dictionary allows for easy retrieval of data in the key:value pairs. It also allows for easy interpretation of the data. Choosing this route made it easier for me to visualize the intended output data, as the outer dictionary’s key is the customer number and the value to the key is the spending data of the corresponding customer(key). This challenge handles a lot of information, with this nested dictionary, it allows me to keep track of everything in one data structure, unlike if I were to use a list(s), I would have had to keep track of multiple lists to store different input data, i.e) packs_purchased_spent, dice_purchased_spent, etc.

    What didn’t work and my solution:
One thing that didn’t work for me was the calculation of the value for packs_spent. I was very content with my code with my for loop calculating all the customer’s spent money, but was troubled when I would run the tests and they would all come back not passed. I didn’t realize at the time that I only calculated the value for packs_spent with the pack price of 4.25. It wasn’t until I reread the problem statement that I forgot about the other price concerning trading cards (36 packs for 125.00). Realizing this, I created an if-else statement for if the packs purchased were greater than or equal to 36 and if they were not. Thankfully, this if-else statement was able to calculate the correct amount spent for packs_purchased whether it be 5 packs sold or 76.


    When code didn’t perform as expected:
One part of my code that didn’t perform as expected was the last part that dealt with who the highest paying customer(s) were. While it did output a value. It continually failed tests as it would not output more than 1 customer. This became a problem when more than 1 customer had the highest spending amount. For a while I was stumped on how to include all the highest paying customers. My first solution was to just append the value to a list. But what I learned was that the list continued to hold stale values (previously highest spending customers) even after a bigger value was added to it. I finally found my solution by simply refreshing the list in the for-loop when there is a bigger total_spent value customer. This allowed for a new list to be created each time a bigger (not the same) customer’s total was presented. However, my optimal solution would be to instead of refreshing the list every time, I would like to delete the stale customer in the list and update the existing list.


    Sample Code and Control Flow:

biggest_customer_total_spent = -1
list_of_highest_spending_customers = []
    
for customer in customers:
      if customers[customer]["total_spent"] >= biggest_customer_total_spent:
            if customers[customer]["total_spent"] == biggest_customer_total_spent:
                list_of_highest_spending_customers.append(customer)
            else:
                list_of_highest_spending_customers = [ ]
                list_of_highest_spending_customers.append(customer)
            biggest_customer_total_spent = customers[customer]["total_spent"]


    Control Flow:
-Define variable, biggest_customer_total_spent
-Create list, list_of_highest_spending_customer
-Using for-loop for dictionaries customers
-Loop through each customer number (key of the customers dictionary)
-Get the total_spent value for the current customer
-If the total_spent value for the current customer is great than or equal to biggest_customer_total_spent:
-And
-If the total_spent value for the current customer is equal to the biggest_customer_total_spent, append current customer number to list_of_highest_spending_customer
-Else: refresh the list, list_of_highest_spending_customer,
-Append current customer to list_of_highest_spending_customer
-Update the Biggest_customer_total_spent is to total_spent value for the current customer
"""


def sales_summary(packs_purchased, dice_purchased, board_games_purchased):
    """
    Parameters:
      packs_purchased: How many packs of trading cards each customer purchased.
      dice_purchased: How many sets of dice were each customer purchased.
      board_games_purchased: How many board games each customer purchased.
    """
    print("Welcome to the Ada's Game Emporium Sales Tracker!")
    print()

    # Price for each category
    packs_price = 4.25
    bundle_pack_price = 125.00
    dice_price = 11.00
    games_price = 50.00
    
    # initialize customers dictionary
    # Customers dictionary will have customer number (1,2,3,...) as the key
    # and customer's spending data as the value for each key.
    customers = {}
    
    # Calculate the number of customers with packs_purchased
    # since the number of the elements in the packs_purchased is the number of the total customers.
    number_of_customers = len(packs_purchased)
    
    # For each customer...
    for i in range(number_of_customers):
        # initialize dictionary for each customer
        # each customer dictionary will have "packs_spent", "dice_spent", "board_games_spent", and "total_spent" as keys
        # and will have the amount spent as the values for each key.
        customers[i + 1] = {}
        
        # Calculate price of total packs purchased
        # If there are more than 36 packs purchased,
        # calculate how many bundle(36 packs) were purchased
        # and calcuate the total based on bundle purchased
        # else: (no bundles), calculate the total packs purchased with normal pack purchased price.
        if packs_purchased[i] >= 36:
            bundle_pack = int(packs_purchased[i]/36)
            customers[i +1]["packs_spent"] = bundle_pack * bundle_pack_price + (packs_purchased[i]-(bundle_pack * 36)) * packs_price
        else:
            customers[i + 1]["packs_spent"] = packs_price * packs_purchased[i]
        
        # Calculate the total spent for dice purchased for each customer
        customers[i + 1]["dice_spent"] = dice_price * dice_purchased[i]
        
        # Calculate the total spent for board games purchased for each customer
        customers[i + 1]["board_games_spent"] = games_price * board_games_purchased[i]
        
        # Calculate the total amount spent by each customer by adding all the spendings
        customers[i + 1]["total_spent"] = customers[i + 1]["packs_spent"] + customers[i + 1]["dice_spent"]+ customers[i +1]["board_games_spent"]
    
    # Add each customer's total spending to the overall_total_spent
    overall_total_spent = 0
    
    # Add each customer's total non-trading card spending to the overall_non_trading_card_total
    overall_non_trading_card_total = 0
    
    # Keeps track of the biggest customer total spent for all customers
    biggest_customer_total_spent = -1
       
    # Keeps track of the highest spending customers
    list_of_highest_spending_customers = []
    
    #For each keys, customer number, in customers dictionary
    for customer in customers:
        print("Customer " + str(customer) + " spent $"+ str(format(customers[customer]["total_spent"],'.2f')))
        print(">>> $" + str(format(customers[customer]["packs_spent"],'.2f')) + " for trading card packs")
        print(">>> $" + str(format(customers[customer]["dice_spent"],'.2f')) + " for dice sets")
        print(">>> $" + str(format(customers[customer]["board_games_spent"],'.2f')) + " for board games")
        print()
        
        # Add each of the customers total spending to get the overall total spending
        overall_total_spent += customers[customer]["total_spent"]
        
        # Add each of the customers non-trading total spending to get the overall non-trading spending
        overall_non_trading_card_total += (customers[customer]["dice_spent"] + customers[customer]["board_games_spent"])
        
        # If the current customer's total spending is bigger than or equal to the previous biggest customer total spent,
        # update the biggest_customer_total_spent to the current customer's total spending
        # and add the highest spending customer to the list_of_highest_spending_customers list.
        if customers[customer]["total_spent"] >= biggest_customer_total_spent:
            if customers[customer]["total_spent"] == biggest_customer_total_spent:
                list_of_highest_spending_customers.append(customer)
            else:
                list_of_highest_spending_customers = [ ]
                list_of_highest_spending_customers.append(customer)
            biggest_customer_total_spent = customers[customer]["total_spent"]


                
            
        
   
    
    print("Combined all customers paid $" + str(format(overall_total_spent,'.2f')) + " total" )
    print("Non-trading card products (dice + board games) were $" + str(format(overall_non_trading_card_total,'.2f')) + " total")
    
    print()
    print("$" + str(format(biggest_customer_total_spent,'.2f')) + " was the most paid by any single customer")
    # Format Output for 'The customer(s) that paid the most were:'
    if len(list_of_highest_spending_customers) == 1:
        print("The customer(s) that paid the most were: #" + str(list_of_highest_spending_customers[0]))
    else:
        output_string = ""
        for i in range(0,len(list_of_highest_spending_customers)):
            output_string += " #" + str(list_of_highest_spending_customers[i])
            # Only add comma at the end of each output string if we are not at the last customer in the list_of_highest_spending_customers list.
            if i != len(list_of_highest_spending_customers) -1:
                output_string += ","
        print("The customer(s) that paid the most were:" + output_string)
