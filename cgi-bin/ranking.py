#!/usr/bin/env python3
import cgi
from mysql_utils import get_connection
from queries import name_lookup

def print_ranks():
    connection = get_connection()
    sql = """select combatant_one, combatant_two, winner_id, DATE_FORMAT(start, '%Y-%m-%d %T'),
             TIMESTAMPDIFF(SECOND, start, finish) from fight order by start;"""

    cursor = connection.cursor()
    cursor.execute(sql)

    #Do stuff

    cursor.close()
    connection.close()

def main():


if __name__ == "__main__":
    main()
