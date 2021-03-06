#!/usr/bin/env python3
import cgi
from mysql_utils import get_connection


"""
    print_combatants() is a function responsible for creating links to cgi script
        which generate a page displaying details about the combatant.  It does this for
        every combatant in the database.
"""

def print_combatants():

    connection = get_connection()
    sql = "SELECT id, name FROM combatant"
    cursor = connection.cursor()

    cursor.execute(sql)

    #Format string stores the id as cid for cgi to pull it later
    name_link_fmt = """<a href='combatantid.py?cid={0}'>{1}</a>"""

    for combatantId, name in cursor.fetchall():
        print("<br/>")
        print(name_link_fmt.format(combatantId, name))

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
    print("<br/><br/><a href='../index.html'>home page</a>")
    print("</center>")
    print("</body></html>")

if __name__ == "__main__":
    main()
