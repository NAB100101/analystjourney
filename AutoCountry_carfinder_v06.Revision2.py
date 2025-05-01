# AutoCountry Vehicle Finder v0.6 launch
# This program allows the user to select options from display menu
# Vehicle list of authorized vehicles can be modified and saved to file
from pathlib import Path

vehicle_file = "vehicles.txt"
file_path = Path(vehicle_file)

# Vehicle list
authorized_vehicles = [
    "Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck",
    "Toyota Tundra", "Rivian R1T", "Ram 1500"
]

# Initialize file
def initialize_vehicle_file(file_path, vehicles):
    if file_path.exists():
        print("File exists!")
    else:
        print("File does not exist. Creating file...")
        with file_path.open('w') as file:
            for vehicle in vehicles:
                file.write(vehicle + '\n')
        print("Vehicle file created.")

# Load from file
def load_vehicles_from_file(file_path):
    if not file_path.exists():
        return []
    with file_path.open('r') as file:
        return [line.strip() for line in file.readlines()]

# Save to file
def save_vehicles_to_file(file_path, vehicle_list):
    with file_path.open('w') as file:
        for vehicle in vehicle_list:
            file.write(vehicle + '\n')

# Menu display
def display_menu():
    print("*******************************")
    print(" Welcome to AutoCountry's Vehicle Finder v0.6")
    print("*******************************")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")
    print("6. DISPLAY updated Authorized Vehicle List ")
    print("*******************************")

# Raw list
def print_list_authorized_vehicles(file_path):
    vehicles = load_vehicles_from_file(file_path)
    for vehicle in vehicles:
        print(vehicle)

# Search
def search_vehicle(file_path, vehicle_to_search):
    vehicles = load_vehicles_from_file(file_path)
    search_key = vehicle_to_search.strip().lower()
    if any(v.lower() == search_key for v in vehicles):
        print(f'"{vehicle_to_search}" is an authorized vehicle.\n')
    else:
        print(f'"{vehicle_to_search}" is NOT an authorized vehicle.\n')

# Add
def add_vehicle(file_path, new_vehicle):
    vehicles = load_vehicles_from_file(file_path)
    new_vehicle_clean = new_vehicle.strip()
    if any(v.lower() == new_vehicle_clean.lower() for v in vehicles):
        print(f'"{new_vehicle}" is already in the list.\n')
    else:
        vehicles.append(new_vehicle_clean)
        save_vehicles_to_file(file_path, vehicles)
        print(f'"{new_vehicle}" has been added.\n')

# Delete
def delete_vehicle(file_path, vehicle_to_delete):
    vehicles = load_vehicles_from_file(file_path)
    search_key = vehicle_to_delete.strip().lower()
    updated_vehicles = [v for v in vehicles if v.lower() != search_key]
    if len(updated_vehicles) != len(vehicles):
        save_vehicles_to_file(file_path, updated_vehicles)
        print(f'"{vehicle_to_delete}" has been removed.\n')
    else:
        print(f'"{vehicle_to_delete}" was not found.\n')

# Main menu
def main():
    initialize_vehicle_file(file_path, authorized_vehicles)
    while True:
        display_menu()
        choice = input("Enter choice (1-6): ").strip()
        if choice == '1':
            print_list_authorized_vehicles(file_path)
        elif choice == '2':
            name = input("Enter the vehicle name to search: ").strip()
            search_vehicle(file_path, name)
        elif choice == '3':
            name = input("Enter the name of the vehicle to add: ").strip()
            add_vehicle(file_path, name)
        elif choice == '4':
            name = input("Enter the name of the vehicle to delete: ").strip()
            delete_vehicle(file_path, name)
        elif choice == '5':
            print("Thank you for using the AutoCountry Vehicle Finder. Goodbye!")
            break
        elif choice == '6':
            print_list_authorized_vehicles(file_path)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
# Run
if __name__ == "__main__":
    main()