# Display welcoming message to user
print("Welcome to AutoCountry where you can find your next vehicle from our large inventory.")

# Allowed vehicles array
allowed_vehicles =["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
for vehicle in allowed_vehicles:
    print(vehicle)

# Prompt user to make selection by inputting full name of vehicle from list    
allowed_vehicles.append
def search_vehicle():
    search_name = input("\n** Please Enter the full vehicle name: ")
    if search_name in allowed_vehicles:
        print(f" {search_name} is FOUND for purchase in the allowed vehicle list.")
    else:
        print(f" {search_name} is NOT FOUND in the allowed vehicle list.")
search_vehicle()
        
#  Decision structure
response = input("Please enter a number from 0 to 4: ")
if (not response.isnumeric()):
    print(response + "is not a number. Please try again.")
else:
    index= int(response)
    if 0 <= index < len(allowed_vehicles):    
        print("You selected:", allowed_vehicles[index])
        print("Thank you for choosing AutoCountry Vehicle Finder to help you find your next vehicle!")
    else:    
        print("The number is out of range. Please enter a number from 0 to 4.")
index = int(input("\nPlease enter the number of the vehicle you want from 0 to 4: "))
# Display selection
print("You selected:", allowed_vehicles[index])
print("Thank you for choosing AutoCountry Vehicle Finder to help you find your next vehicle")