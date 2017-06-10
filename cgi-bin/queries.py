#!/usr/bin/env python3
from mysql_utils import get_connection

def select_combatant(combatantId):

    connection = get_connection()
    cursor = connection.cursor()
    sql = """select combatant.id, combatant.name, species.name, type, (base_atk + plus_atk),
             (base_dfn + plus_dfn), (base_hp + plus_hp) from combatant, species 
             where combatant.id = %s and species.id = species_id"""

    cursor.execute(sql, [combatantId])

    row = cursor.fetchone()
    cursor.close()
    connection.close()
    return row

def get_record(combatantId):
    connection = get_connection()
    cursor = connection.cursor()
    sql = """ select COUNT(combatant_one) as 'wins' from fight where winner_id = %s"""

    cursor.execute(sql, [combatantId])
    wins = cursor.fetchone()
    wins = wins[0]

    sql = """select COUNT(combatant_one) as 'total' from fight
             where (combatant_one = %s or combatant_two = %s);"""

    variables = (combatantId, combatantId)
    cursor.execute(sql, variables)
    total = cursor.fetchone()
    total = total[0]

    cursor.close()
    connection.close()
    return (wins, total)

def name_lookup(lookup_id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = """select name from combatant where id = %s"""

    cursor.execute(sql, [lookup_id])
    name = cursor.fetchone()
    name = name[0]

    cursor.close()
    connection.close()
    return name
    
