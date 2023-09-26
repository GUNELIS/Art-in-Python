Measurements Exercise
=====================

This git repository is a very simple project, it loads a CSV - file
that contains dummy measurement data. 
This exercise is simple, but it could very well be code that we receive from a customer.

After reading the measurement data it calculates the averages and 
prints the result to a simple table. 
It might not be a very useful script, but it could very well be a script written by a customer. 

There are some things in this script that can be improved, that's the 
goal of this exercise. Please complete the tasks below and save the steps to
separate files, so that it's easy to compare the differences and the progress becomes visible. 
We're using a git repository here, so you can use it as you deem fit. 

1. When you execute the script (python ./read_measurements.py) you'll see 
   that the experiment_A is listed twice, do you know why and can you solve it?

2. When I execute the script from the parent directory (python ./measurements/read_measurements.py") 
   I get the following error: 

    Traceback (most recent call last):
      File "./measurements/read_measurements.py", line 35®, in <module>
        with open('./measurements.csv') as data_file:
    IOError: [Errno 2] No such file or directory: './measurements.csv'

   Do you know what is wrong and can you solve it? (Assuming that measurements.csv is in the same directory as read_measurements.py)

3. Now the script can only read './measurements.csv', please modify the script
   so that you can specify the file as an argument. 

4. This script is written in a difficult and inefficient way, can you try to 
   make modifications so that: 

   - it's easier to understand
   - it's more efficient 

   (there are many possible answers to this question, the reasoning is more important 
    than the end result, so make sure to document your decisions and tradeoffs)


