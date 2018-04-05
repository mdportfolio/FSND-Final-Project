# FSND-Final-Project
## Log Analysis Project

### Project Description: 
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

### What you need:
* Vagrant installed 
* Virtual box for Windows installed 

#### How to run the program on Windows:
1. Access git on your computer.
2. Change directories `cd` command
3. When you reach the folder with the Vagrant file, put the `vagrant up` command.
4. Now that you have the VM booted up, put the `winpty vagrant ssh` command.
You should see the `vagrant@vagrant:` prompt. This means that you are in the VM.
5. In the VM, change directories until you reach your file with the queries.
`cd (folder of python file)`
`python (python_file.py)`

#### How to load the database:
1. Download the FSND zip folder from the project instructions.
2. One of the file inside is called newsdata.sql. Extract the file into the vagrant directory, which is shared with your virtual machine.
3. Start your Virtual Machine(VM)._(Refer to previous section.)_
4. After you load the VM, you should see`vagrant@vagrant/vagrant:`
5. In the prompt, load the database to the VM with this command`psql -d news -f newsdata.sql` or `psql -d news`
Here's a breakdown of the command:
* `psql` — the PostgreSQL command line program
* `-d news` — connect to the database named news which has been set up for you
* `-f newsdata.sql` — run the SQL statements in the file newsdata.sql
6. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
