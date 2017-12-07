# ADS-Module-Page

## To Run the project clone this repository and open a terminal and run the following
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## If you don't have PostgreSQL installed on your machine, do the following (Ubuntu specific)
```
sudo nano /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc
sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-9.6
```

### Setup a new password

```
sudo nano /etc/postgresql/9.1/main/pg_hba.conf
```
change
```
local   all             postgres                                peer
```
to
```
local   all             postgres                                trust
```
```
sudo service postgresql restart
psql -U postgres
ALTER USER postgres with password 'your-pass';
```
Now change it back
```
sudo nano /etc/postgresql/9.1/main/pg_hba.conf
```
```
local   all             postgres                                trust
```
to
```
local   all             postgres                                md5
```
Finally, change the SQLALCHEMY_DATABASE_URI in main.py based on your configuration.

### Create a new database
```
sudo service postgresql restart
psql
(In psql cli)
create database module_page
```

## If you have not created the tables or database schema is modified?, do below steps to re-create it. 
```
    python reinitdb.py
```

## Some Common Database Operations.
```
# View all tables
\dt

# View table schema
\d+ table_name;

# View content of a table
select * from table_name;

# Delete data from a table
truncate table table_name;
```

Make sure that ssl.key and ssl.crt are created, then run
```
python main.py
```

Now access
https://localhost:5000 
to see the Homepage.
