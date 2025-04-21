# Display welcoming message to user
print("Welcome to AutoCountry where you can find your next vehicle from our large inventory")

# Authorized vehicles array to be displayed to user
authorized_vehicles = ["Ford F-150","Chevrolet Silverado","Tesla CyberTruck","Toyota Tundra","Nissan Titan"]
for vehicle in authorized_vehicles:
    print(vehicle)

# Assign cooresponding numbers to makes avaliable in inventory and display output
makes = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]

# Prompt the user to enter a number from the range and validate input
response = input("Please enter a number from 0 to 4: ")

# Decision structure and output
if (not response.isnumeric()):
    print(response + "is not a number. Please try again.")
else:
    index= int(response)
    if 0 <= index < len(makes):    
        print("You selected:", makes[index])
        print("Thank you for choosing AutoCountry Vehicle Finder to help you find your next vehicle")
    else:    
        print("The number is out of range. Please enter a number from 0 to 4.")
 

