#!/usr/bin/env python
# coding: utf-8

# What is data base and what is difference between SQL and NOSQL data base?

# A database is an organized collection of structured information, or data, typically stored electronically in a computer system.
# 
# SQL databases are relational, and NoSQL databases are non-relational.
# SQL databases use structured query language (SQL) and have a predefined schema. NoSQL databases have dynamic schemas for unstructured data.
# SQL databases are vertically scalable, while NoSQL databases are horizontally scalable.
# SQL databases are table-based, while NoSQL databases are document, key-value, graph, or wide-column stores.
# SQL databases are better for multi-row transactions, while NoSQL is better for unstructured data like documents or JSON.

# What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
# 

# Data Definition Language(DDL) is a subset of SQL and a part of DBMS(Database Management System). DDL consist of Commands to commands like CREATE, ALTER, TRUNCATE and DROP. These commands are used to create or modify the tables in SQL.

# CREATE :
# This command is used to create a new table in SQL. The user has to give information like table name, column names, and their datatypes.

# CREATE TABLE Student_info
# (
# College_Id number(2),
# College_name varchar(30),
# Branch varchar(10)
# );

# 

# ALTER :
# This command is used to add, delete or change columns in the existing table. The user needs to know the existing table name and can do add, delete or modify tasks easily.

# ALTER TABLE table_name
# ADD column_name datatype;

# TRUNCATE :
# This command is used to remove all rows from the table, but the structure of the table still exists.

# TRUNCATE TABLE table_name;

# DROP :
# This command is used to remove an existing table along with its structure from the Database.

# DROP TABLE table_name;

# What is DML? Explain INSERT, UPDATE, and DELETE with an example.
# 

# The structured query language (SQL) commands deal with the manipulation of data present in the database that belongs to the DML or Data Manipulation Language.

# INSERT
# Insert command is used to insert data into a table.
# Insert into <table_name> (column list) values (column values);

# DELETE
# Delete command is used to delete records from a database table.

# Delete from <table_name>WHERE condition;

# 

# UPDATE
# Update command is used to update existing data within a table.

# UPDATE <table_name> SET column_number =value_number WHERE condition;

# What is DQL? Explain SELECT with an example.
# 

# Query languages, often known as DQLs or Data Query Languages, are computer languages that are used to make various queries in information systems and databases. The Structured Query Language (SQL) is a well-known example. DQL statements are used to query the data contained in schema objects.

# The SELECT command is used to query or retrieve data from a table in the database. It is used to retrieve a subset of records from one or more tables. The SELECT command can be used in various forms:
# 
# 

# Syntax of SELECT command :
# 
# SELECT <column-list> FROM<table-name>;

# Explain Primary Key and Foreign Key.
# 

# Keys are one of the most important elements in a relational database to maintain the relationship between the tables and it also helps in uniquely identifying the data from a table. The primary Key is a key that helps in uniquely identifying the tuple of the database whereas the Foreign Key is a key that is used to identify the relationship between the tables through the primary key of one table that is the primary key one table acts as a foreign key to another table.

# Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
# 

# In[3]:


import mysql.connector


# In[1]:


pip install MySQL Connector


# In[2]:


import mysql.connector


# In[3]:


pip install mysql-connector-python


# In[4]:


import mysql.connector


# In[6]:


import mysql.connector

my_hosts = ["mysql-host1", "mysql-host2"] # List all your hosts names/IPs here

hosts_with_default_password = []
for host in my_hosts:
    try:
        mydb = mysql.connector.connect(
        host=host,
        user="yourusername",
        password="yourpassword")
        hosts_with_default_password.append(host)
    except Exception as e:
        print('Failed to connect to host {}'.format(host))

print(hosts_with_default_password)


# A cursor is a data access object that can be used to either iterate over the set of rows in a table or insert new rows into a table.

# Give the order of execution of SQL clauses in an SQL query.

# The order in which the clauses in queries are executed is as follows:
# 
# 1. FROM/JOIN: The FROM and/or JOIN clauses are executed first to determine the data of interest.
# 
# 2. WHERE: The WHERE clause is executed to filter out records that do not meet the constraints.
# 
# 3. GROUP BY: The GROUP BY clause is executed to group the data based on the values in one or more columns.
# 
# 4. HAVING: The HAVING clause is executed to remove the created grouped records that don’t meet the constraints.
# 
# 5. SELECT: The SELECT clause is executed to derive all desired columns and expressions.
# 
# 6. ORDER BY: The ORDER BY clause is executed to sort the derived values in ascending or descending order.
# 
# 7. LIMIT/OFFSET: Finally, the LIMIT and/or OFFSET clauses are executed to keep or skip a specified number of rows.

# In[ ]:




