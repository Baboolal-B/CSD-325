"""

Brijette Baboolal
2/02/2025
Baboolalmiles_to_kilometerspt2.py

This program uses a function to convert miles to kilometers. 
It prompt the user for the number of miles driven then call 
a function which converts miles to kilometers.

"""

def miles_to_kilometers(miles):
    #Converts miles to kilometers.
    return miles * 1.60934  # Conversion factor from miles to kilometers


def get_miles_input():
    #Prompts the user for miles driven and validates input.
    while True:
        try:
            # Prompt user for input
            miles = float(input("Enter the number of miles driven: "))
            if miles < 0:
                print("Please enter a non-negative number.")  # Ensure input is non-negative
                continue
            return miles
        except ValueError:
            print("Invalid input. Please enter a numeric value.")  # Handle non-numeric input


def main():
    # Get user input
    miles = get_miles_input()
    # Convert miles to kilometers
    kilometers = miles_to_kilometers(miles)
    # Display the result
    print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")


if __name__ == "__main__":
    main()  # Run the main function