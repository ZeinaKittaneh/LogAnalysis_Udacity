#! /usr/bin/python2

import psycopg2

DBNAME = "news"
question1 = "\nWhat are the most popular three articles of all time?\n"
query1 = '''SELECT
    title,
    COUNT(substr(path, 10)) AS views
FROM
    articles
    JOIN
        log
        ON slug = substr(path, 10)
GROUP BY
    title
ORDER BY
    views DESC LIMIT 3;'''

question2 = "\nWho are the most popular article authors of all time?\n"
query2 = '''SELECT
    auth.name,
    SUM(views_qry.views)
FROM
    authors auth,
    articles artic,
    (
        SELECT
            title,
            COUNT(substr(path, 10)) AS views
        FROM
            articles
            JOIN
                log
                ON slug = substr(path, 10)
        GROUP BY
            title
    )
    views_qry
WHERE
    auth.id = artic.author
    AND views_qry.title = artic.title
GROUP BY
    auth.name
ORDER BY
    SUM(views_qry.views) DESC;'''

question3 = "\nOn which days did more than 1% of requests lead to errors?\n"
query3 = '''SELECT
    *
FROM
    (
        SELECT
            total.DAY,
            round(CAST((error.errorCount*100) AS NUMERIC) /
            CAST(total.totalCount AS NUMERIC), 2) AS percentage
        FROM
            (
                SELECT
                    DATE(TIME) AS DAY,
                    COUNT(*) AS errorCount
                FROM
                    log
                WHERE
                    status NOT LIKE '%200 OK%'
                GROUP BY
                    DAY
            )
            AS error
            INNER JOIN
                (
                    SELECT
                        DATE(TIME) AS DAY,
                        COUNT(*) AS totalCount
                    FROM
                        log
                    GROUP BY
                        DAY
                )
                AS total
                ON total.DAY = error.DAY
    )
    AS subqry
WHERE
    percentage > 1.0;'''


def get_top_articles(cursor):
    print (question1)
    cursor.execute(query1)
    results = cursor.fetchall()
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def get_popular_author(cursor):
    print(question2)
    cursor.execute(query2)
    results = cursor.fetchall()
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')


def get_day_max_error(cursor):
    print(question3)
    cursor.execute(query3)
    results = cursor.fetchall()
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + '%')


if __name__ == '__main__':
    conn = psycopg2.connect(dbname=DBNAME)
    cursor = conn.cursor()
    get_top_articles(cursor)
    get_popular_author(cursor)
    get_day_max_error(cursor)
    conn.close()
