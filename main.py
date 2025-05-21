import pandas as pd
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os
import sys

# Set up argument parsing
parser = argparse.ArgumentParser(description="Process data with an optional data path.")
parser.add_argument('--data_path', type=str, default='data',
                    help='Path to the data file.')
args = parser.parse_args()

# Read in dataset that I made in google sheets
try:
    table = pd.read_csv(args.data_path)
except FileNotFoundError:
    print(f"Error: The data file '{args.data_path}' was not found.")
    sys.exit(1)

# Verify essential columns
essential_columns = ['Attendance', 'Team', 'Year']
for column_name in essential_columns:
    if column_name not in table.columns:
        print(f"Error: Essential column '{column_name}' not found in {args.data_path}.")
        print("This script is designed for NBA attendance data, similar to the 'data' file provided.")
        sys.exit(1)

pd.set_option("display.max_columns", None)
r_squared_values = []

# Create plots directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Define columns to exclude from predictors
excluded_columns = ['Team', 'Year', 'Attendance']

# Create a line of regression by setting the explanotory
# variable as the x value and attendance as the y
for col_name in table.columns:
    if col_name in excluded_columns:
        continue  # Skip excluded columns
    string = col_name
    x = table.loc[:,string]
    y = table.loc[:,"Attendance"]
    res = stats.linregress(x, y)
    # Create a scatterplot
    plt.plot(x, y, 'o', label='original data')
    # Create a line of regression according to the scatterplot
    plt.plot(x, res.intercept + res.slope * x, 'r', label='fitted line')
    plt.legend()
    # Add labels to the graph
    plt.title(""+ string + " and Fan Attendance")
    plt.xlabel(string)
    plt.ylabel("Fans")
    # Save the plot to a file
    plot_filename = f"plots/{string}_and_Fan_Attendance.png"
    plt.savefig(plot_filename)
    plt.clf()  # Clear the figure for the next plot


    # Calculate correlation coefficient using built-in Scipy functions
    r = stats.pearsonr(x, y)[0]
    print("Correlation Coefficient for " + string+" and Fans:")
    print(r)
    print()
    print("Correlation of Determination:")
    print(r * r)
    print()
    r_squared_values.append(r*r)


print(r_squared_values)




