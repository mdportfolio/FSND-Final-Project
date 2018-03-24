import psycopg2
from datetime import datetime

def authors_question():
	"""Prints the authors and their views"""
	connect = psycopg2.connect("dbname = news ")
	cursor = connect.cursor()
	cursor.execute("""SELECT name, COUNT(status) AS views FROM authors, log, articles WHERE articles.author = authors.id GROUP BY authors.id ORDER BY views DESC;""")
	answer = cursor.fetchall()
	print('Who are the most popular article authors of all time?')
	print('"' + str(answer[0][0]) + '"' + '-'+ str(answer[0][1]) + "" +'views')
	print('"' + str(answer[1][0]) + '"' + '-'+ str(answer[1][1]) + "" +'views')
	print('"' + str(answer[2][0]) + '"' + '-'+ str(answer[2][1]) + "" +'views')
	print('"' + str(answer[3][0]) + '"' + '-'+ str(answer[3][1]) + "" +'views')
	connect.close()	

def articles_question():
	"""Prints the authors and their views"""
	connect = psycopg2.connect("dbname = news")
	cursor = connect.cursor()
	cursor.execute("""SELECT title, COUNT(status) AS views FROM articles, log WHERE RIGHT(log.path, -9) = articles.slug GROUP BY articles.title ORDER BY views DESC LIMIT 3;""")
	answer = cursor.fetchall()
	print('What are the most popular articles of all time?')
	print('"' + str(answer[0][0]) + '"' + '-'+ str(answer[0][1]) + "" +'views')
	print('"' + str(answer[1][0]) + '"' + '-'+ str(answer[1][1]) + "" +'views')
	print('"' + str(answer[2][0]) + '"' + '-'+ str(answer[2][1]) + "" +'views')
	connect.close()	

def error_question ():	
	"""Prints the day with an error greater than 1%"""
	connect = psycopg2.connect("dbname = news")
	cursor = connect.cursor()
	cursor.execute("""SELECT date_part('month', time) m, date_part('day', time) d, date_part('year',time) y, SUM(CASE status WHEN '200 OK' THEN 0 ELSE 1 END)/COUNT(status) AS percentage FROM log GROUP BY log.time HAVING SUM(CASE status WHEN '200 OK' THEN 0 ELSE 1 END)/COUNT(status) > 0.01 ORDER BY d;""")
	answer = cursor.fetchall()
	print('On which days did more than 1%' + " " +'of requests lead to errors?')	
	result = answer[0]
	
authors_question()
articles_question()
error_question ()
