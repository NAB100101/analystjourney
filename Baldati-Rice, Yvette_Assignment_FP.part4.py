# Program welcoming message and user options from menu
def display_menu():
    print("Welcome to AutoCountry's Vehicle Finder v0.4")
    print("***************")
    print("Please enter the following number below from the following menu: ")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    
# Defining vehicles function
def print_vehicles(vehicles):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in vehicles:
        print(vehicle)

# User input for vehicle search
def search_vehicle(vehicles):
    search_name = input("Enter the vehicle name to search: ")
    if search_name in vehicles:
        print(f'"{search_name}" is an authorized vehicle.')
    else:
        print(f'"{search_name}" is NOT an authorized vehicle.')
# User adding vehicle to list
def add_vehicle(vehicles):
    vehicle_name = input("Please Enter the full Vehicle name you would like to add: ")
    vehicles.append(vehicle_name)
    print(f'You have added "{vehicle_name}" as an authorized vehicle')
# User deletion of vehicle from list    
def delete_vehicle(vehicles):
    vehicle_name = input("Please enter the full Vehicle name you would like to delete: ")
    if vehicle_name in vehicles:
        confirm = input(f'Are you sure you want to remove "{vehicle_name}" from the Authorized Vehicles List? (yes/no) ')
        if confirm.lower() == 'yes':
            vehicles.remove(vehicle_name)
            print(f'You have REMOVED "{vehicle_name}" as an authorized vehicle')
    else:
        print(f'"{vehicle_name}" is NOT in the authorized list.')
# Allowed vehicles list and decision structure
def main():
    allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck','Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print_vehicles(allowed_vehicles)
        elif choice == '2':
            search_vehicle(allowed_vehicles)
        elif choice == '3':
            add_vehicle(allowed_vehicles)
        elif choice == '4':
            delete_vehicle(allowed_vehicles)
        elif choice == '5':
            print("You are now exiting AutoCountry's Vehicle Finder. Thank you for choosing us in your new vehicle journey.")
            break
        else:
            print("Invalid input. Please choose a number from the menu.")

# Run of the updated program
main()