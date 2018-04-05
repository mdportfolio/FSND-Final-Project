#! /usr/bin/env python
import psycopg2
from datetime import datetime


def authors_question():

    """Prints the authors and their views"""

    connect = psycopg2.connect("dbname = news ")
    cursor = connect.cursor()
    cursor.execute("""SELECT authors.name, COUNT(*) AS views
    FROM authors, log, articles
    WHERE authors.id = articles.author and
    log.path = concat('/article/', articles.slug)
    GROUP BY authors.name ORDER BY views DESC;""")
    answer = cursor.fetchall()
    print('Who are the most popular article authors of all time?')
    for (writer, count) in answer:
        print ("{} - {} views".format(writer, count))
    connect.close()


def articles_question():

    """Prints the authors and their views"""

    connect = psycopg2.connect("dbname = news")
    cursor = connect.cursor()
    cursor.execute("""SELECT title, COUNT(status) AS views
    FROM articles, log WHERE RIGHT(log.path, -9) = articles.slug
    GROUP BY articles.title
    ORDER BY views DESC LIMIT 3;""")
    answer = cursor.fetchall()
    print ('What are the most popular articles of all time?')
    for (writer, count) in answer:
        print ("{} - {} views".format(writer, count))
    connect.close()


def error_question():

    """Prints the day with an error greater than 1%"""

    connect = psycopg2.connect("dbname = news")
    cursor = connect.cursor()
    cursor.execute("""SELECT date_part('month', time) m,
    date_part('day', time) d, date_part('year',time) y,
    SUM(CASE status WHEN '200 OK' THEN 0 ELSE 1 END)
    /COUNT(status) AS percentage FROM log GROUP BY log.time
    HAVING SUM(CASE status WHEN '200 OK' THEN 0 ELSE 1 END)/
    COUNT(status) > 0.01 ORDER BY d;""")
    answer = cursor.fetchall()
    print (
     'On which days did more than 1%' + " " + 'of requests lead to errors?')
    results = list(set(answer))
    for date in results:
        print ('{:%M-%d-%Y}'.format(datetime(date)))
    connect.close()


authors_question()
articles_question()
error_question()
