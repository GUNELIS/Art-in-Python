"""
In this task I chose to break down the script into 4 different componenets where each one
performs a different task: 
(1) Reading, (2) Organizing, (3) Calculating and (4) Printing.
This is done to ensure good Readability as each function has a discriptive name and defined purpose. 
It also allows for easier debugging and updating (if tests are involved) and some functions can be 
used for different puropses. In general, this way the code is easier to understand, test,
update and modify which saves development time in the long run.  

Note: There is a tradeoff here, using many functions can introduce some complexity and confusion 
especially if the parameters are not manged correctly. However, in this use case this seems to be 
the correct way to go. 
"""

import csv


def load_csv_data(file):
    """
    This function uses the built in CSV reader to parse the data, 
    the function takes in the path of the file and returns the 
    first row (name, power, temp, # of cats, # of dogs) as well as the data itself.
    Using 'csv' is good as it handles edge cases and ensures safer parsing.  
    """
    try:
        with open(file, 'r') as data_file:
            reader = csv.reader(data_file)
            categories = next(reader)
            return categories, list(reader)
    except FileNotFoundError:
        print(f"File '{file}' not found. Please enter the correct path.")

def organize_experiments(data_rows):
    """
    This function is used to organize each experiment by the name of it.
    It is done by making use of a dictionary where the experiment name is the key and
    the experiment data is the value. This is more efficient and clearer. In this case, looking
    through the experiments by name is a lot faster than iterating trough the whole list.
    """

    experiments = {} # Establishing a experiments dictionary

    for row in data_rows:
        name = row[0].strip() # stripping the spaces in the names (task1)
        data = [float(item) for item in row[1:]] # converting the strings to floats and storing them in a list
       
        if name not in experiments: # if we have yet to see this experiment we create a new key
            experiments[name] = []

        experiments[name].append(data)  # relating this data list to the relevant name of the experiment
    return experiments


def compute_averages(experiments):
    """
    This function uses the organized experiments dictionary and calculates the average
    value for each column in that experiment only. The fact that the experiments dict
    is organized by name helps to seperate the calculations. 
    The function checks each columns corresponding to a name and gets the averages by transposing 
    the rows into columns (*data). 
    """

    averages = {}
    for name, data in experiments.items():  # for each experiment
        exp_avg = []   # create a list containing the avergae value for each column
        for col in zip(*data):  # lets get each columnm (power, temp, cats, dogs)
            exp_avg.append(sum(col) / len(col))  # calculate the average for each column of that experiment

        averages[name] = exp_avg   # add the average list to the avergaes dictionary 
    return averages 



def show_results(header, experiment_averages):
    """
    Using this function for printing and visualizing. 
    """

    print("\t".join(header))
    print("=" * 80)
    for name, averages in experiment_averages.items():
        print(name + "\t" + "\t".join(map(str, averages)))


# here we can simply call all the functions by order and see results.
if __name__ == "__main__":
    path = input("Please enter the path to the CSV file: ")
    header, data_rows = load_csv_data(path)
    experiments = organize_experiments(data_rows)
    experiment_averages = compute_averages(experiments)
    show_results(header, experiment_averages)


