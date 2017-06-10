#!/usr/bin/env python3
import cgi
from mysql_utils import get_connection
from queries import name_lookup

def print_ranks():
    connection = get_connection()
    sql = """select winner_id, COUNT(winner_id) from fight group by winner_id order by winner_id ASC;"""

    cursor = connection.cursor()
    cursor.execute(sql)

    print("<table style='width:40%'>")
    print("<tr>")
    print("<th>#</th>")
    print("<th>Combatant</th>")
    print("<th>Wins</th>")
    print("</tr>")

    index_fmt = """<td>{0}.</td>"""
    name_link_fmt = """<td><a href='combatantid.py?cid={0}'>{1}</a></td>"""
    wins_fmt = """<td>{0}</td>"""

    for index, row in enumerate(cursor.fetchall()):
        combatant_name = name_lookup(row[0])

        print("<tr>")
        print(index_fmt.format(index+1))
        print(name_link_fmt.format(row[0], combatant_name))
        print(wins_fmt.format(row[1]))
        print("</tr>")


    print("</table>")

        

    cursor.close()
    connection.close()

def main():
    print("Content-type: text/html\n")
    print("<html><head><title>Rankings</title>")
    print("<style> table, th, td { border: 0.5px solid black; }</style>")
    print("</head>")
    print("<body><center>")
    print_ranks()
    print("<a href=../index.html>home page</a>")
    print("</center></body></html>")


if __name__ == "__main__":
    main()
