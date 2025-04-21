# Welcoming announcement
def display_menu():
    print("Welcome to AutoCountry's Vehicle Finder v0.3")
allowed_vehicles =["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]
for vehicle in allowed_vehicles:
    def print_vehicles(vehicles):
        print (allowed_vehicles)    
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles:
        print(vehicle)
# Prompt user to search vehicle and determine if vehicle is authorize for sale    
def search_vehicle(vehicles):
    search_name = input("Enter the vehicle name to search: ")
    if search_name in vehicles:
        print(f'"{search_name}" is an authorized vehicle.')
    else:
        print(f'"{search_name}" is NOT an authorized vehicle.')
# Modify authorized vehicles list
def add_vehicle(vehicles):
    vehicle_name = input("Please Enter the full Vehicle name you would like to add: ")
    vehicles.append(vehicle_name)
    print(f'You have added "{vehicle_name}" as an authorized vehicle')
# User input and decision structure
def main():
    allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck','Toyota Tundra', 'Nissan Titan']
    
    while True:
        display_menu()
        choice = input()
        if choice == '1':
            print_vehicles(allowed_vehicles)
        elif choice == '2':
            search_vehicle(allowed_vehicles)
        elif choice == '3':
            add_vehicle(allowed_vehicles)
        elif choice == '4':
            print(allowed_vehicles)
            print("You are now exiting AutoCountry's Vehicle Finder. Thank you for making choosing us in your new vehicle journey.")
            break
        else:
            print("Invalid input. Please choose a number from the menu.")
main()