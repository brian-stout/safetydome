#!/usr/bin/env python3
import cgi
from mysql_utils import get_connection
from queries import name_lookup


"""
    print_ranks() is a function that generates tables based on the ranking standings of
        the combatants.
"""

def print_ranks():
    connection = get_connection()

    #Gets a count of how many times an Id has appeared in the winner_id column
    sql = """select winner_id, COUNT(winner_id) from fight group by winner_id order by winner_id
             ASC;"""

    cursor = connection.cursor()
    cursor.execute(sql)

    print("<table style='width:40%'>")
    print("<tr>")
    #What standing the combatant is
    print("<th>#</th>")
    #WThe combatant's name
    print("<th>Combatant</th>")
    #How many wins the combatant has
    print("<th>Wins</th>")
    print("</tr>")

    #Displays the index with a dot
    index_fmt = """<td>{0}.</td>"""
    #format string used to generate a link to the combatant's detail page
    name_link_fmt = """<td><a href='combatantid.py?cid={0}'>{1}</a></td>"""
    #Simple format for displaying the wins nuber in <td> tags
    wins_fmt = """<td>{0}</td>"""

    #Iterates through each row and index keeps count of which row it's on
    for index, row in enumerate(cursor.fetchall()):
        combatant_name = name_lookup(row[0])

        print("<tr>")
        #Plus on since there's no #0 spot
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
