import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as p
from scipy import stats

rng = np.random.default_rng()

# Read in dataset that I made in google sheets

table = pd.read_csv(r"data")
pd.set_option("display.max_columns", None)
influence = []


# Create a line of regression by setting the explanotory
# variable as the x value and attendance as the y
# Ignore first 3 columns (Team, Year, Response variable)
for i in range(3,len(table.columns)):
    string = table.columns[i]
    x = table.loc[:,string]
    y = table.loc[:,"Attendance"]
    res = p.stats.linregress(x, y)
    # Create a scatterplot
    plt.plot(x, y, 'o', label='original data')
    # Create a line of regression according to the scatterplot
    plt.plot(x, res.intercept + res.slope * x, 'r', label='fitted line')
    plt.legend()
    # Add labels to the graph
    plt.title(""+ string + " and Fan Attendance")
    plt.xlabel(string)
    plt.ylabel("Fans")
    plt.show()


    # Calculate correlation coefficient using built-in Scipy functions
    r = p.stats.pearsonr(x, y)[0]
    print("Correlation Coefficient for " + string+" and Fans:")
    print(r)
    print()
    print("Correlation of Determination:")
    print(r * r)
    print()
    influence.append(r*r)


print(influence)




