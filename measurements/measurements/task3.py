
"""
For this task I chose the input() function which will ask for the path from the user in the 
terminal and then using a try/except block, if the path exists the code script will run 
and if it is caught then an error message will be shown.  

You can examin this by copying the full path of any of your favorite csv files and 
inputting them in the terminal when asked to add a csv path.  
"""


path = input("Please enter the path to the CSV file: ")

try:
    with open(path) as data_file:
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

except FileNotFoundError:
    print(f"File '{path}' not found. Please enter the correct path.")