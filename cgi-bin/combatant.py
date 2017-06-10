#!/usr/bin/env python3
import cgi
from mysql_utils import get_connection

def print_combatants():
    connection = get_connection()
    sql = "SELECT id, name FROM combatant"
    cursor = connection.cursor()

    cursor.execute(sql)

    name_link_fmt = """<li><a href='combatantid.py?cid={0}'>{1}</a></li>"""

    print("<ul>")
    for combatantId, name in cursor.fetchall():
        print(name_link_fmt.format(combatantId, name))
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
    print_combatants()
    print("</center>")
    print("</body></html>")

if __name__ == "__main__":
    main()
