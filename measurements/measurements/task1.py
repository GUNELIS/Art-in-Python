"""
I  n order to solve this problem, 
I chose to use strip() here to clear out any spaces before or after the name 
so that 'experiment_A' and ' experiment_A' are associated in the same group. 
Of course changing the values in csv could have been done as well but this 
is not a good practice as I am looking to prevent this happening in 
future cases as well as keeping the integrity of the results.

Using Strip:
"""

with open('./measurements.csv') as data_file:
    data = data_file.read()
data = data.splitlines()
experiments = []
for cnt, line in enumerate(data):
    if cnt == 0:
        header_values = line.split(',')
    else:
        experiment_data = line.split(',') 
        name = experiment_data[0].strip()   # here I use strip to remove spaces before and after
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

