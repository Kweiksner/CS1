'''
Author; Kaki Weiksner
Data: 3/15/26
Description: Creates multiple graphs for numbers in the Collatz Conjecture and groups of multiples.
Bugs: none
Sources: matplotlib help: https://matplotlib.org/stable/tutorials/pyplot.html, Stats: https://stackoverflow.com/questions/31455470/definition-of-standard-error-in-scipy-stats-linregress, https://docs.scipy.org/doc/scipy-1.2.3/reference/generated/scipy.stats.linregress.html
'''

#imports libraries from computer
import sys
import pandas as pd                 #type: ignore
import matplotlib.pyplot as plt     #type: ignore
import numpy as np                  #type: ignore
import statistics
from scipy.stats import linregress  #type: ignore


def iseven(number):
    '''
    Description: determines if a number is even

    Args:
        number(int): Number that the computer will determine if even or odd

    Returns:
        "odd"(str): the number is odd
        "even"(str): the number is even 
    '''
    if number % 2 == 0:
        return("even")
    else:
        return("odd")
    
def collatz(number):
    '''
    Description: multiples by 3x+1 or divides by, depending if the number is even or odd

    Args:
        number(int): Number that the computer will operate on 

    Returns:
         number(int): new number after operation is performed 
    '''
    even = iseven(number)
    if even == "even": 
        number = number//2
        return(number)
    elif even == "odd":
        number = number * 3 + 1
        return(number)

def sorted_dic(data):
    '''
    Description: sorts a dictionary 
    Args:
        data(dict): dictionary with numbers 
    Returns:
        sorted_data(dict): new dictionary that is sorted 
    '''
    
    #sorts dictionary from highest to lowest 
    sorted_items = sorted(data.items(), key=lambda item: item[1])
    sorted_data = dict(sorted_items)
    return(sorted_data)

def add_dictionary(data_dict,number, iterations):
    data_dict[number] = iterations
    return data_dict

def multiple_to_1000000(all_numbers,means,medians, ranges, LOBF_slope, multiple):
    '''
    Description: Goes though one multiple for the multiple option

    Args:
        all_numbers(dict): dictionary of all numbers that have been used 
        means(dict): dictionary of all means that have already been calculated
        medains(dict): dictionary of all medians that have already been calculated
        ranges(dict): dictionary of all  ranges that have already been calculated
        LOBF_slope(dict): dictionary of all slopes that have already been calculated
        multiples(int): the multiple that the program is going through
    Returns:
        all_numbers(dict): dictionary of all numbers that have been used 
        means(dict): dictionary of all means that have already been calculated
        medains(dict): dictionary of all medians that have already been calculated
        ranges(dict): dictionary of all  ranges that have already been calculated
        LOBF_slope(dict): dictionary of all slopes that have already been calculated
    '''
    data = {}
    multiples = multiple
    for number in range(multiples, multiples*100000+1, multiples):                   #iterates through first 1000 multiples
        iterations = 0
        ori_number = number
        
        while number != 1:
            #if the number has already been calculated then iterations is added to what has already been calculated
            if number in all_numbers:  
                iterations += all_numbers[number] 
                break 
            number = collatz(number)
            iterations += 1
        add_dictionary(data, ori_number, iterations)                           #adds all data to a dictionary 
        all_numbers[ori_number] = iterations                                   #puts the orginal number into all numbers 
        
    #creates x, and y so data can be graphed
    numbers = list(data.keys())
    iterations_list = list(data.values()) 
    x = np.array(numbers)
    y = np.array(iterations_list)


    #sorts all the data
    sorted_data = sorted_dic(data)

    #gets all of the statistics
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    mean = sum(data.values()) / len(data)
    means[multiple] = mean
    median = statistics.median(iterations_list)
    medians[multiple] = median
    rang =list(sorted_data.values())[0]-  list(sorted_data.values())[-1]
    ranges[multiple] = rang
    vals = list(sorted_data.values())
    rang = vals[-1] - vals[0]     
    ranges[multiple] = rang

    LOBF_slope[multiple] = slope    
    
    print()
    print(f"Iterations Statistics for {multiple}")
    print(f"Mean: {mean} ")
    print(f"Median: {median} ")
    print(f"Range: {rang} ")
    print(f"Equation: y = {slope:.4f}x + {intercept:.2f}")
    print(f"Correlation coefficient (r): {r_value:.4f}")
    
    return all_numbers,means,medians, ranges, LOBF_slope

def multiple_first_100000(all_numbers,means,medians, ranges, LOBF_slope, multiple):
    '''
    Description: Goes though one multiple for the multiple option

    Args:
        all_numbers(dict): dictionary of all numbers that have been used 
        means(dict): dictionary of all means that have already been calculated
        medains(dict): dictionary of all medians that have already been calculated
        ranges(dict): dictionary of all  ranges that have already been calculated
        LOBF_slope(dict): dictionary of all slopes that have already been calculated
        multiples(int): the multiple that the program is going through
    Returns:
        all_numbers(dict): dictionary of all numbers that have been used 
        means(dict): dictionary of all means that have already been calculated
        medains(dict): dictionary of all medians that have already been calculated
        ranges(dict): dictionary of all  ranges that have already been calculated
        LOBF_slope(dict): dictionary of all slopes that have already been calculated
    '''
   
    data={}
    multiples = multiple
    for number in range(multiples, multiples*100000+1, multiples):                   #iterates through first 1000 multiples
        iterations = 0
        ori_number = number
        
        while number != 1:
            #if the number has already been calculated then iterations is added to what has already been calculated
            if number in all_numbers:  
                iterations += all_numbers[number] 
                break 
            number = collatz(number)
            iterations += 1
        add_dictionary(data, ori_number, iterations)                           #adds all data to a dictionary 
        all_numbers[ori_number] = iterations                                   #puts the orginal number into all numbers 
        
    #creates x, and y so data can be graphed
    numbers = list(data.keys())
    iterations_list = list(data.values()) 
    x = np.array(numbers)
    y = np.array(iterations_list)


    #sorts all the data
    sorted_data = sorted_dic(data)

    #gets all of the statistics
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    mean = sum(data.values()) / len(data)
    means[multiple] = mean
    median = statistics.median(iterations_list)
    medians[multiple] = median
    rang =list(sorted_data.values())[0]-  list(sorted_data.values())[-1]
    ranges[multiple] = rang
    vals = list(sorted_data.values())
    rang = vals[-1] - vals[0]     
    ranges[multiple] = rang

    LOBF_slope[multiple] = slope    
    
    #print()
    #print(f"Iterations Statistics for {multiple}")
    #print(f"Mean: {mean} ")
    #print(f"Median: {median} ")
    #print(f"Range: {rang} ")
   # print(f"Equation: y = {slope:.4f}x + {intercept:.2f}")
   # print(f"Correlation coefficient (r): {r_value:.4f}")
    
    return all_numbers,means,medians, ranges, LOBF_slope

def create_graphs(means, medians, ranges, LOBF_slope,title):
    '''
    Description: creates four graphs using the means, medians and ranges for all multiples 
    Args:
        means(dict): dictionary of all means that have already been calculated
        medains(dict): dictionary of all medians that have already been calculated
        ranges(dict): dictionary of all  ranges that have already been calculated
        LOBF_slope(dict): dictionary of all slopes that have already been calculated
    Returns:
        void: shows all graphs 
    '''

    multiples = list(means.keys())
    mean_values = list(means.values())
    median_values = list(medians.values())
    range_values = list(ranges.values())
    slope_values = list(LOBF_slope.values())
    
    # Create a figure with 4 subplots (2x2 grid)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(title, fontsize=16, fontweight='bold')
    
    # Graph 1: Means
    axes[0, 0].plot(multiples, mean_values, marker='o', linestyle='-', linewidth=2, markersize=8, color='blue')
    axes[0, 0].set_xlabel('Multiple', fontsize=11)
    axes[0, 0].set_ylabel('Mean Iterations', fontsize=11)
    axes[0, 0].set_title('Mean Iterations vs Multiple', fontsize=12)
    axes[0, 0].grid(True, alpha=0.3)
    
    # Graph 2: Medians
    axes[0, 1].plot(multiples, median_values, marker='o', linestyle='-', linewidth=2, markersize=8, color='green')
    axes[0, 1].set_xlabel('Multiple', fontsize=11)
    axes[0, 1].set_ylabel('Median Iterations', fontsize=11)
    axes[0, 1].set_title('Median Iterations vs Multiple', fontsize=12)
    axes[0, 1].grid(True, alpha=0.3)
    
    # Graph 3: Ranges
    axes[1, 0].plot(multiples, range_values, marker='^', linestyle='-', linewidth=2, markersize=8, color='red')
    axes[1, 0].set_xlabel('Multiple', fontsize=11)
    axes[1, 0].set_ylabel('Range', fontsize=11)
    axes[1, 0].set_title('Range vs Multiple', fontsize=12)
    axes[1, 0].grid(True, alpha=0.3)
    
    # Graph 4: LOBF Slopes
    axes[1, 1].plot(multiples, slope_values, marker='D', linestyle='-', linewidth=2, markersize=8, color='purple')
    axes[1, 1].set_xlabel('Multiple', fontsize=11)
    axes[1, 1].set_ylabel('Slope', fontsize=11)
    axes[1, 1].set_title('Line of Best Fit Slope vs Multiple', fontsize=12)
    axes[1, 1].grid(True, alpha=0.3)

   #displays the graphs  
    plt.tight_layout()
    plt.show()

def stats_to_csv(means, medians, ranges, LOBF_slope, filename='collatz_stats.csv'):
    '''
    Description: Saves all statistics to CSV using pandas
    '''

    # Combine all dictionaries into a DataFrame
    all_dictionaries = pd.DataFrame({
        'multiple': list(means.keys()),
        'mean': list(means.values()),
        'median': list(medians.values()),
        'range': list(ranges.values()),
        'slope': list(LOBF_slope.values())
    })
    
    all_dictionaries.to_csv(filename, index=False)

def one(all_numbers):
    means={}
    medians={}
    ranges={}
    LOBF_slope={}

    for i in range(1, 129,2):                                                                                           #goes through every multiple
        all_numbers,means,medians, ranges, LOBF_slope = multiple_first_100000(all_numbers,means,medians, ranges, LOBF_slope, 0+i)

    title = ("First 100,000 multiples for all multiples 1-128 Odds")
    create_graphs(means, medians, ranges, LOBF_slope,title)
    stats_to_csv(means, medians, ranges, LOBF_slope, 'first_100000_multiples_Odds.csv')


def two(all_numbers):
    all_numbers = {}
    means={}
    medians={}
    ranges={}
    LOBF_slope={}

    for i in range(1, 129,2):                                                                                           #goes through every multiple
        all_numbers,means,medians, ranges, LOBF_slope = multiple_to_1000000(all_numbers,means,medians, ranges, LOBF_slope, 0+i)  
    
    title = ("Multiples 1-128 up to 10,000,000 Odds") 
    create_graphs(means, medians, ranges, LOBF_slope,title)
    stats_to_csv(means, medians, ranges, LOBF_slope, 'multiples_to_10000000_Odds.csv')

def main():
    all_numbers = {}
    one(all_numbers)
    two(all_numbers)
    
main()