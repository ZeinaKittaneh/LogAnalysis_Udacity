#!/usr/bin/env python3

import psycopg2

DBNAME = "news"
q1 = "\nWhat are the most popular three articles of all time?\n"
ans1 = '''select title, count(substr(path, 10)) as views from articles join log
on slug = substr(path, 10) group by title order by views desc limit 3;'''

q2 = "\nWho are the most popular article authors of all time?\n"
ans2 = '''select auth.name, sum(views_qry.views) from authors auth,
articles artic, ( select title, count(substr(path, 10)) as views from articles
join log on slug = substr(path, 10) group by title) views_qry where
auth.id = artic.author and views_qry.title = artic.title group by auth.name
order by sum(views_qry.views) desc;'''

q3 = "\nOn which days did more than 1% of requests lead to errors?\n"
ans3 = '''select * from (
select total.day,
round(cast((error.errorCount*100) as numeric) / cast(total.totalCount
as numeric), 2) as percentage from
(select date(time) as day, count(*) as errorCount from log where status
not like '%200 OK%' group by day) as error
inner join
(select  date(time) as day, count(*) as totalCount from log group by day)
as total on total.day = error.day) as subqry
 where percentage > 1.0;'''


def solve_q1():
    conn = psycopg2.connect(dbname=DBNAME)
    cursor = conn.cursor()
    print q1
    cursor.execute(ans1)
    results = cursor.fetchall()
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')
    conn.close()


def solve_q2():
    conn = psycopg2.connect(dbname=DBNAME)
    cursor = conn.cursor()
    print(q2)
    cursor.execute(ans2)
    results = cursor.fetchall()
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')
    conn.close()


def solve_q3():
    conn = psycopg2.connect(dbname=DBNAME)
    cursor = conn.cursor()
    print(q3)
    cursor.execute(ans3)
    results = cursor.fetchall()
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + '%')
    conn.close()

if __name__ == '__main__':
    solve_q1()
    solve_q2()
    solve_q3()
