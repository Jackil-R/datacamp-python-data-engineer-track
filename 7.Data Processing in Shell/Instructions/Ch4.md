#Chapter 4 - ata Pipeline on the Command Lin2


## Finding Python version on the command line
Which of the following commands will NOT show what version of Python is installed? Feel free to try out the various answers on the terminal.
#### Instructions
- python
- python -V
- python --version
- Answer: which python

#Executing Python script on the command line
Let's work through an example of how we can use Python on the command line without needing to open up a GUI like Jupyter Notebook or Spyder. Interacting with Python on the command line is faster and more efficient than using a GUI. Here, we will create a Python file and execute it using our native Python, all without leaving the bash terminal.
#### Instructions
- In one step, create a new Python file and pass the Python print command into the file.
- Execute the new Python file by calling it directly from the command line.


## Understanding pip's capabilities
Which of the following statements regarding pip is NOT true?

Feel free to try out the various answers on the terminal.
#### Instructions
- Print the pip version the same way as the Python version, using option flag --version
- pip can be used to upgrade itself using pip install --upgrade pip
- pip can be used to install csvkit since it is written in Python
- Answer: pip can only install one Python package at a time

## Installing Python dependencies
In the following exercises, we will work through the set up process for making sure our Python environment has the proper library dependencies installed prior to executing a Python model script. In this pipeline we will create the requirements.txt file which houses the dependencies we need to install, install the dependencies, and do a quick sanity check to make sure everything is properly set up.
#### Instructions
- Instantiate the requirements.txt document and add the scikit-learn library to the requirements.txt file.
- Use pip to install the dependencies in the requirements.txt file.
- Use pip to list what Python libraries are already installed in your environment.

## Running a Python model
n the previous exercise, we installed the packages necessary to run a Python model script. In this exercise, we'll run a pre-written Python script create_model.py which will output two things: a Python model in a saved .pkl file and the predicted scores in a saved .csv file.
#### Instructions
- Use pip to list and verify that the libraries specified in create_model.py have been installed.
- Run the Python script create_model.py from the command line.

## Understanding cron scheduling syntax
Which of the following is the correct Crontab syntax for execute the Python model script (model.py) every hour, on the 15 minute of an hour? (e.g. 12:15 PM, 1:15 AM, 2:15 AM, etc)?

Remember the syntax for Crontab:
``````
.---------------- minute (0 - 59)
|  .------------- hour (0 - 23)
|  |  .---------- day of month (1 - 31)
|  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
|  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed ...
|  |  |  |  |
*  *  *  *  * command-to-be-executed
``````
#### Instructions
- * * * * * python model.py
- Answer:1 5 * * * * python model.py
- 15 * * * python model.py
- 15 * * * * model.py


## Scheduling a job with crontab
In this exercise, we will create a simple Python job and automate this job using CRONTAB so that it runs every minute.

If you're unsure of how to use cron or crontab, refer to https://crontab.guru for more documentation.
#### Instructions
- Verify that there are currently no CRON jobs currently scheduled via CRONTAB.
- Create a Python file called hello_world.py which prints "hello world" when executed.
- Modify CRONTAB by adding a job that runs the Python script hello_world.py every minute on the minute.
- Verify that the CRON job has been created successfully.


## Model production on the command line
Often times, Python models, once perfected, need to be moved into production and run on a frequent basis. To save the data scientist's time, instead of running the model manually every day, the run process is automated.

Automating and putting a Python model into production involves first installing all necessary library dependencies, running the Python model itself, and then setting a schedule for frequency of the runs. While it is possible to do all these steps separately using different languages and programs, consolidating all efforts into command line commands allows for more user control and easier automation.

In this capstone exercise, we will practice how to set up an end-to-end Python script automation process step by step.
#### Instructions
- Use pip to install the Python dependencies listed in the requirements.txt file.
- Now that the necessary Python dependencies have been installed, run the create_model.py script on the command line.
- We have verified that the Python model can be run. Next step is to automate this job so it runs every minute. Use CRONTAB to schedule a per minute run of the Python script create_model.py.
- Print the job scheduled in CRONTAB to verify that the CRON job is scheduled correctly.

## Course recap

#### Instructions