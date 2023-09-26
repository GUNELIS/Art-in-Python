import os

"""
The Problem:

The  open() function works with the directory from which the script is being run, 
in this case the user is trying to run the script from the parent directory 
but measurements.csv doesn't exist in that directory, but in the measurements 
sub directory (ill call it the child directory).

Solution: 
When approaching this assignment the first solution that came to mind was to change the line: 
"with open('./measurements.csv') as data_file:" 
to: 
"with open('./measurements/measurements.csv') as data_file:"

This allows the user coming from the parent directory to run the script,
but not from the child directory.

I decided to allow the script to be run regradless if it is executed from 
parent directory or the child directory. This is done by using os module which gets 
the path of the script's directory.
Then using the os join() function to construct the final path with the 
known name : 'measurenents.csv'.

To run from parent dir: 'python ./measurements/task2.py'
To run from parent dir: 'python task2.py'
"""

script_dir = os.path.dirname(os.path.abspath(__file__))   # get the path of the directory running this script 

final_path = os.path.join(script_dir, 'measurements.csv')  # Construct the final path with the known csv name 

# now the script can run from both parent and child dir

with open(final_path) as data_file:
    data = data_file.read()

data = data.splitlines()
experiments = []
for cnt, line in enumerate(data):
    if cnt == 0:
        header_values = line.split(',')
    else:
        experiment_data = line.split(',') 
        name = experiment_data[0].strip()
        experiment_exists = False
        # search for existing experiment
        for experiment in experiments: 
            # experiment already exists
            if experiment[0] == name:
                experiment_exists = True
                # add new data to existing experiment
                experiment.append(experiment_data[1:])

        if not experiment_exists:
            # add new experiment
            experiments.append([name, experiment_data[1:]])


# calculate the averages
experiment_averages = []
for experiment in experiments:
    name = experiment[0]
    data = experiment[1:]
    averages = [float(data[0][i]) for i in range(len(data[0]))]

    cnt = 1.
    for experiment_data in data[1:]:
        cnt += 1
        for i in range(len(experiment_data)):
            averages[i] += float(experiment_data[i])

    averages = [avg / cnt for avg in averages]
    experiment_averages.append([name, averages])

print("\t".join(header_values))
print("=" * 40)
for name, averages in experiment_averages:
    print(name + "\t" + "\t".join(map(str, averages)))

