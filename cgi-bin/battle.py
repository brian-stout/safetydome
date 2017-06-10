#!/usr/bin/env python3
import cgi
from mysql_utils import get_connection
from queries import name_lookup
from extra_output import time_string

def print_battles():
    connection = get_connection()
    sql = """select combatant_one, combatant_two, winner_id, DATE_FORMAT(start, '%Y-%m-%d %T'),
             TIMESTAMPDIFF(SECOND, start, finish) from fight order by start;"""

    cursor = connection.cursor()
    cursor.execute(sql)

    print("<table style='width:80%'>")
    print("<tr>")
    print("<th>Match Link</th>")
    print("<th>First Combatant</th>")
    print("<th>Second Combatant</th>")
    print("<th>Victor</th>")
    print("<th>Start Time</th>")
    print("<th>Match Length </th>")
    print("</tr>")

    battle_link_fmt = """<td style='text-align:center'><a href='battledetails.py?cmbt1={0}&cmbt2={1}&victor={2}&str_time={3}&length={4}'>{5}.</a></td>"""

    name_link_fmt = """<td><a href='combatantid.py?cid={0}'>{1}</a></td>"""

    for index, row in enumerate(cursor.fetchall()):
        combatant_1 = name_lookup(row[0])
        combatant_2 = name_lookup(row[1])

        if row[2] == row[0]:
            victor = combatant_1
        elif row[2] == row[1]:
            victor = combatant_2
        else:
            victor = "Error! Victor data corruption!"

        time_elapsed = time_string(row[4])

        print("<tr>")
        print(battle_link_fmt.format(combatant_1,combatant_2,victor,row[3], time_elapsed, index))
        print(name_link_fmt.format(row[0], combatant_1))
        print(name_link_fmt.format(row[1], combatant_2))
        print(name_link_fmt.format(row[2], victor))
        print("<td>" + row[3] + "</td>")
        print("<td>" + time_elapsed + "</td>")
        print("</tr>")

    print("</table>")

    cursor.close()
    connection.close()

def main():
    # This is the Head of the HTTP response
    print("Content-type: text/html\n")


    #This begins the Body of hte HTTP Response
    print("<html><head><title>Battles</title>")
    print("<style> table, th, td { border: 0.5px solid black; }</style>")
    print("</head>")
    print("<body>")
    print("<center>")

    print_battles()

    print("</center>")
    print("</body></html>")

if __name__ == "__main__":
    main()

