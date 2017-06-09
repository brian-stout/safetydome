#!/usr/bin/env python3
import cgi
from mysql_utils import get_connection
fields = cgi.FieldStorage()
default = ""

def select_field():
    connection = get_connection()
    sql = "SELECT NAME FROM species"
    cursor = connection.cursor()

    cursor.execute(sql)
    names = cursor.fetchall()

    print("<ul>")
    for name in names:
        print("<li>" + name[0] + "</li>")
    print("</ul>")

    cursor.close()
    connection.close()

def main():

    # This is the Head of the HTTP response
    print("Content-type: text/html\n")


    #This begins the Body of hte HTTP Response
    print("<html><head><title>Combatants</title></head>")
    print("<body>")
    print("<center>")
    print("<h1> Current fighters in the WSDL! </h1>")
    select_field()
    print("</center>")
    print("</body></html>")

if __name__ == "__main__":
    main()