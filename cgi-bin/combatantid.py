#!/usr/bin/env python3
import cgi
from mysql_utils import get_connection
fields = cgi.FieldStorage()
default = ""
combatantId = fields.getvalue("cid", default)

def select_combatant(combatantId):
    connection = get_connection()
    sql = "SELECT * FROM combatant WHERE id = %s"
    cursor = connection.cursor()
    cursor.execute(sql, [combatantId])
    row = cursor.fetchone()
    print(row)

def main():

    # This is the Head of the HTTP response
    print("Content-type: text/html\n")

    #This begins the Body of hte HTTP Response
    print("<html><head><title>Combatant Title</title></head>")
    select_combatant(combatantId)
    print("<body>")
    print("</body></html>")

if __name__ == "__main__":
    main()

