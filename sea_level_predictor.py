import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df["CSIRO Adjusted Sea Level"] = df["CSIRO Adjusted Sea Level"].fillna(0)
    # Clean the data by removing rows with missing values
    df = df.dropna(subset=["Year", "CSIRO Adjusted Sea Level"])
    
    x = df.Year.values.tolist()
    y = df["CSIRO Adjusted Sea Level"].values.tolist()

    # Create scatter plot
    plt.scatter(x, y, label='original data')

    # Create first line of best fit
    res = linregress(x, y)
    x_res = np.linspace(min(x), 2050, num=171)
    
    y_res = res.intercept + res.slope * x_res
    plt.plot(x_res, y_res, 'r', label='fitted line from data since 1993')

    # Create second line of best fit
    x_since_2000 = x[120 :]
    y_since_2000 = y[120 :]
    res_since_2000 = linregress(x_since_2000, y_since_2000)
    x_res_2000 = np.linspace(2000, 2050, num=51)
    y_res_2000 = res_since_2000.intercept + res_since_2000.slope * x_res_2000
    
    plt.plot(x_res_2000, y_res_2000, 'b', label='fitted line from data since 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
