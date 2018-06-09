# Logs_Analysis

## Introduction

- In this project a highly complex data base with millions of rows is explored using the complex sql queries.

- Several SQL queries are written using PostgreSQL 

- SQL Statements  such as SELECT, Joins, Aggregate functions, Joins and Views were used to perform the tasks.

- This Project replicates the internal reporting site for the news paper article to know the interest of the user

- The database has the server logs and newspaper articles of the site.

#### The project gives following conclusions:
* Most popular three articles of all time.
* Most popular article authors of all time.
* Days on which more than 1% of requests lead to errors.

## Technologies Required

- Python
- PostgreSQL
- Vagrant
- VirtualBox


### Environment Required

- The virtual environment has to be created using Vagrant and Virtual Box

- The Data is Extracted from the file newsdata.sql (psql -d news -f newsdata.sql) to run the sql statements

### Steps Required

- Download fsnd-virtual machine document

- vagrant init

- vagrant up

- vagrant ssh

- cd /vagrant

- python3 newsdata.py


## Views Used

* <h4>allstatus</h4>

```sql
create view allstatus as select time :: date , status from log;
```

* <h4>failstatus</h4>

```sql
CREATE VIEW failstatus as select time, count(*) as num from allstatus where status like '%404%' group by time;
```

* <h4>finalstatus</h4>

```sql
create view finalstatus as select time, count(*) as num from allstatus where status like '%404%' or status like '%200%' group by time;
```
* <h4>percentage</h4>
```sql
create view percentage as select finalstatus.time, finalstatus.num, failstatus.num:: double precision/finalstatus.num:: double precision * 100 AS failpercent from finalstatus, failstatus where finalstatus.time = failstatus.time;
```









