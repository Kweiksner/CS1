import sys
import pandas as pd                 #type: ignore
import matplotlib.pyplot as plt     #type: ignore
import numpy as np                  #type: ignore
import statistics
from scipy.stats import linregress  #type: ignore

def iseven(number):
    if number % 2 == 0:
        return("even")
    else:
        return("odd")

def collatz(number):
    even = iseven(number)
    if even == "even": 
        number = number/2
        return(number)
    elif even == "odd":
        number = number * 3 + 1
        return(number)

def check_integer(number):
    try:
        number = int(number)
    except ValueError:
        return "False"
    return number

def get_number():
    while True:
        number = input("Enter a multiple (Enter stop to stop code):")
        isinteger = check_integer(number)
        if number == "stop":
            sys.exit()
        elif isinteger == "wrong input":
            print("You did not enter a number")
        else:
            number = isinteger
            return(number)

def add_dictionary(data_dict,number, iterations):
    data_dict[number] = iterations
    return data_dict

def create_graph(numbers, iterations_list, x, y, line_x, line_y, mean, median, rang, slope, intercept, r_2, r_value):
    plt.figure(figsize=(10, 6))
    plt.plot(numbers, iterations_list, marker='o', linestyle='', markersize=8, label='Data points')  # Changed iterations to iterations_list
    
    # Add line of best fit
    plt.plot(line_x, line_y, color='red', linestyle='--', linewidth=2, 
             label=f'Best fit: y={slope:.4f}x+{intercept:.2f}')

    # Add labels and title with R² value
    plt.xlabel('Number', fontsize=12)
    plt.ylabel('Iterations', fontsize=12)
    plt.title(f'Number vs Iterations (R² = {r_2:.4f})', fontsize=14)

    # Add grid and legend
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Add text box with statistics
    textstr = f'Slope: {slope:.4f}\nIntercept: {intercept:.2f}\nR²: {r_2:.4f}\nMean: {mean:.2f}\nMedian: {median:.2f}\nRange: {rang:.2f}'
    plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Display the plot
    plt.show()

def sorted_dic(data):
    sorted_items = sorted(data.items(), key=lambda item: item[1])
    sorted_data = dict(sorted_items)
    return(sorted_data)

def get_mean(data):
    meanval = sum(data.values()) / len(data)
    return meanval 

def get_median(data):
    numbers = list(data.values())
    median = statistics.median(numbers)
    return median 

def get_range(data):
    first_value = list(data.values())[0]
    last_value = list(data.values())[-1]
    rang = last_value - first_value
    return rang

def r_squared(x,y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    r_squared = r_value**2
    return r_squared, r_value

def LOBF(x,y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    line_x = np.array([min(x), max(x)])
    line_y = slope * line_x + intercept
    return line_x, line_y

def intercept_slope(x,y):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return intercept, slope


def main():
    data = {}
    while True:
        multiple = input("Enter multiple:")
        multiple = check_integer(multiple)
        if multiple == "False":
            print("Enter a multiple")
        else:
            break

    for number in range(multiple, multiple*100000+1, multiple): 
        iterations = 0
        ori_number = number
        number = collatz(number)
        while number != 1:
            number = collatz(number)
            iterations += 1
        add_dictionary(data, ori_number, iterations)
    
    numbers = list(data.keys())
    iterations_list = list(data.values()) 
    x = np.array(numbers)
    y = np.array(iterations_list)


    sorted_data = sorted_dic(data)

    mean = get_mean(data)
    median = get_median(data)
    rang = get_range(sorted_data)
    slope, intercept = intercept_slope(x,y)
    line_x, line_y = LOBF(x,y)
    r_2, r_value = r_squared(x,y)
    
    print()
    print(f"Iterations Statistcs for{multiple}")
    print(f"Mean: {mean} ")
    print(f"Median: {median} ")
    print(f"Range: {rang} ")
    print(f"Equation: y = {slope:.4f}x + {intercept:.2f}")
    print(f"R-squared: {r_2:.4f}")
    print(f"Correlation coefficient (r): {r_value:.4f}")

    create_graph(numbers, iterations_list, x,y, line_x, line_y, mean, median, rang,slope, intercept, r_2, r_value)

main()