##Importing the python library to connect to the database

import psycopg2

import datetime

DBNAME = "news"

db = psycopg2.connect(database = DBNAME)

print ("Opened database successfully")

##1. What are the most popular articles of all time?

#def top_articles():

  #db = psycopg2.connect(database = DBNAME)
print("Top three articles:")
c = db.cursor()
c.execute("select articles.title, count(*) as num from log, articles where log.status = '200 OK' and articles.slug = substr(log.path, 10) group by articles.title order by num desc limit 3 ")
articles = c.fetchall()
for title,num  in articles:
	print(" \"{}\" -- {} views".format(title, num))
#db.close()
    


##2. Who are the most popular article authors of all time?

#def top_authors():

print("Top Authors are:")

c2 = db.cursor()
c2.execute("select authors.name, count(*) as num from articles, authors, log where log.status='200 OK' and authors.id = articles.author and articles.slug = substr(log.path, 10) group by authors.name order by num desc")
authors = c2.fetchall()
for name, num in authors:
    #print("The top most authors of all time are:")
    print("{} -- {} views".format(name,num))
#db.close()
  


##3. On which days did more than 1% of requests lead to errors?

print("Day/Days with errors greater than 1 percent is/are:")

c3 = db.cursor()
c3.execute("select time, failpercent from percentage where failpercent > 1")
errors = c3.fetchall()
for day, failpercent in errors:
    #print("The top most authors of all time are:")
    print("""{0:%B %d, %Y} -- {1:.2f} %  errors""".format(day, failpercent))
db.close()




