"""
This program has been modified by Brijette Baboolal
Assignment 4.2
04/04/2025-04/05/2025

This program would allows users to view and analyze weather data 
from a CSV file for the year 2018. It reads data from the file 
sitka_weather_2018_simple.csv, which contains daily temperature readings, 
and then allows users to choose between viewing a plot of the daily high or low temperatures. 
Once the user chooses and option of either high or low temperture the chart would be saved as a 
png to their file when this program is saved. 
"""
import csv  
import sys  
import os  
from datetime import datetime  
import matplotlib  
matplotlib.use('Agg')  # Use a backend that avoids GUI input issues 
from matplotlib import pyplot as plt  

# Load data from the CSV file
filename = 'sitka_weather_2018_simple.csv'  # Name of the weather data file
with open(filename) as f:
    reader = csv.reader(f)  # Create a CSV reader object to parse the file
    header_row = next(reader)  # Skip the header row

    dates, highs, lows = [], [], []  # Initialize empty lists for dates, high temperatures, and low temperatures
    for row in reader:  # Reads through each row in the CSV file
        try:
            # Convert the string representing the date into a datetime object
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])  # Convert the high temperature to an integer
            low = int(row[6])   # Convert the low temperature to an integer
        except ValueError:  # Handle missing or invalid data
            print(f"Missing data for {row[2]}")  # Print a message if data is missing
        else:
            # Append valid data to the corresponding lists
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Function to plot temperatures and save the plot as an image
def plot_temperatures(dates, temps, label, color, filename):
    fig, ax = plt.subplots()  # Create a new figure and axis for the plot
    ax.plot(dates, temps, c=color)  # Plot the temperatures with the specified color
    plt.title(f"Daily {label} Temperatures - 2018", fontsize=24)  # Title of the plot
    plt.xlabel('', fontsize=16)  # Label for the x-axis 
    fig.autofmt_xdate()  # Automatically format the x-axis labels 
    plt.ylabel("Temperature (F)", fontsize=16)  # Label for the y-axis
    plt.tick_params(axis='both', which='major', labelsize=16)  # Set size for tick labels

    # Save the plot to a file
    plt.tight_layout()  # Adjust the layout to prevent clipping of labels
    plt.savefig(filename)  # Save the plot to the specified file
    plt.close()  # Close the plot to free up memory

    # Open the plot image with the default viewer based on the operating system
    if sys.platform.startswith('darwin'):  # For macOS
        os.system(f'open {filename}')
    elif sys.platform.startswith('win'):   # For Windows
        os.system(f'start {filename}')
    elif sys.platform.startswith('linux'):  # For Linux
        os.system(f'xdg-open {filename}')

# Menu loop to interact with the user
print("Welcome to the Weather Viewer!")  # Print welcome message
while True:  # Infinite loop to keep the menu running
    print("\nPlease select an option:")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ").strip()  # Get user input and strip leading/trailing whitespace
    
    if choice == '1':  # If user selects option 1
        plot_temperatures(dates, highs, "High", "red", "highs_plot.png")  # Plot high temperatures
    elif choice == '2':  # If user selects option 2
        plot_temperatures(dates, lows, "Low", "blue", "lows_plot.png")  # Plot low temperatures
    elif choice == '3':  # If user selects option 3
        print("Thanks for using the Weather Viewer. Goodbye!")  # Exit message
        sys.exit()  # Exit the program
    else:  # If user enters an invalid choice
        print("Invalid choice. Please enter 1, 2, or 3.")  # Print error message for invalid choice
