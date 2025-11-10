# SCHOOL DATABASE 

## Project Objective
Create an application that connects to the SQL database to run Create, Read, Update and Delete functions.


## Dependencies
- Python
- PostgreSQL
- psycopg2
    - run "python3 -m pip install psycopg2" 


## Running Instruction
- Go to the project directory
- Create a new database "school"
    - run "createdb school" in your terminal
- Run "psql -U your_username -d school -f database.sql"
- Edit the app.py file and update the database configuration dictionary with your credentials
- To see how the functions work, add a main() in app.py and call the functions with desired values
- Run "python3 app.py" to run the application and see the results