# pylint:disable=C0111,C0103
import sqlite3


def students_from_city(db, city):
    """return a list of students from a specific city"""
    query = """
        SELECT first_name,last_name
        FROM students
        WHERE birth_city = ?
    """
    db.execute(query,(city,))
    result = db.fetchall()
    list_students = [f"{row[0]} {row[1]}" for row in result]
    return list_students


# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py
#
# import sqlite3
conn = sqlite3.connect('data/school.sqlite')
db = conn.cursor()
print(students_from_city(db, 'Paris'))
