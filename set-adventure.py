'''   
Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
You have two sets of flight destinations, one for each airline. 
Write a Python program to find out:

1. Destinations that both airlines fly to.

2. Destinations unique to your airline.

3. Whether there are any destinations that neither airline shares.

Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
'''


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

while True: 
    print("\n1.Compare Routes")
    print("2. Exit") 
    choice = input("Please select your choice: ")
    
    if choice == '1': 
        both_fly = our_routes.intersection(competitor_routes)   # create new set with similar routes for print statement
        print(f"Both airlines fly to {both_fly}") 
        #for route in both_fly:
            #print(f"Both airlines fly to {route}.")
        
        print('')   # space for easy read 
            
        only_us = our_routes.difference(competitor_routes)  # create a new set with routes only found in 'our_routes' 
        print(f"Our airline flies to {only_us}, while out competitor does not")
        #for route in only_us: 
            #print(f"Our airline flies to {route}, while our competitor does not.")
            
        print('')   # space for easy read
        
        each_own = our_routes.symmetric_difference(competitor_routes) # new set with routes unique to each 'our_routes' and 'competitor_routes' 
        for route in each_own:
            if route in our_routes:
                print(f"Our airline flies to {route}.")
            elif route in competitor_routes:
                print(f"Our competitor flies to {route}.") 
    elif choice == '2': 
        break  
    else:
        print("Invalid option, please try again.")