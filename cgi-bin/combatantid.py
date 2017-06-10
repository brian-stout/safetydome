#!/usr/bin/env python3
import cgi
from mysql_utils import get_connection
from queries import get_record
from extra_output import generate_img_tag


"""
    select_combatant() is responsible for grabbing all the relevant fields of a combatant
        given the combatant's unique ID.  The query automatically adds in the plus attributes
        so the user doesn't have to worry about them.
"""

def select_combatant(combatantId):

    #Makes sure combatantId is a digit
    if combatantId.isdigit():
        pass
    else:
        #CGI Script checks to see if the function returned none, if it does it
        #   prints out an appropriate error message in html
        return None

    #Making sure there isn't any negative numbers
    if int(combatantId) <= 0:
        return None

    connection = get_connection()
    cursor = connection.cursor()
    sql = """select combatant.id, combatant.name, species.name, type, (base_atk + plus_atk),
             (base_dfn + plus_dfn), (base_hp + plus_hp) from combatant, species 
             where combatant.id = %s and species.id = species_id"""

    #We're only grabbing one row
    cursor.execute(sql, [combatantId])

    row = cursor.fetchone()
    cursor.close()
    connection.close()
    return row

"""
    print_combatant() is responsible for formatting all the fields from select_combatant()
        into a useable html table.
"""

def print_combatant(row, record):
        print("<table style='width:30%'>")

        #Displays the fighter's name and ID as a header
        print("<tr>")
        print("<th>" + row[1] + "</th>")
        print("<th> ID: " + str(row[0]) + "</th>")
        print("</tr>")

        #A row that displays the fighter's species
        print("<tr>")
        print("<td style='text-align:justify'>species: </td>")
        print("<td>" + row[2] + "</td>")
        print("</tr>")

        #A row that displays the fighter's type
        print("<tr>")
        print("<td style='text-align:justify'>type:</td>")
        print("<td>" + row[3] + "</td>")
        print("</tr>")

        #A row that displays the fighter's attack rating
        print("<tr>")
        print("<td style='text-align:justify'>attack:</td>")
        print("<td>" + str(row[4]) + "</td>")
        print("</tr>")

        #A row that displays the fighter's defensive rating
        print("<tr>")
        print("<td style='text-align:justify'>defense:</td>")
        print("<td>" + str(row[5]) + "</td>")
        print("</tr>")

        #A row that displays the fighter's max hp
        print("<tr>")
        print("<td style='text-align:justify'>hp:</td>")
        print("<td>" + str(row[6]) + "</td>")
        print("</tr>")

        #A row that displays the number of wins the fighter has
        print("<tr>")
        print("<td style='text-align:justify'>wins:</td>")
        print("<td>" + str(record[0]) + "</td>")
        print("</tr>")

        #A row that displays the number of battles a fighter as been in
        print("<tr>")
        print("<td style='text-align:justify'>total battles:</td>")
        print("<td>" + str(record[1]) + "</td>")
        print("</tr>")

        #Quick row calculating a win loss ratio.
        print("<tr>")
        print("<td style='text-align:justify'>w/l ratio:</td>")
        if (record[1] > 0):
            print("<td>" + str(record[0] / record[1]) + "</td>")
        #If the fighter has never lost but has battles displays 100%
        elif (record[0] > 0):
            print("<td> 1.00 </td>")
        #If the fighter has never had a battle displays no value
        else:
            print("<td> No value </td>")
        print("</tr>")
        
        print("</table>")

def main():

    fields = cgi.FieldStorage()
    default = ""

    #Grabbing the combatantId passed from the other form
    combatantId = fields.getvalue("cid", default)

    #Grabbing the combatant details
    row = select_combatant(combatantId)

    #Grabbing the combatant's record
    record = get_record(combatantId)

    #This is the Head of the HTTP response
    print("Content-type: text/html\n")

    #If both functions successfully returned data display the web page properly
    if row and record:
        #This begins the Body of hte HTTP Response
        print("<html><head><title>WSDL : " + row[1] + "</title>")
        print("<style> table, th, td { border: 1px solid black; }</style></head>")
        print("<body><center>")
        generate_img_tag(row[1])
        print_combatant(row, record)

    #If one of the functions returned None then display an error page
    else:
        print("<html><head><title>Error!</title>")
        print("<body><center>Error grabbing data!")
    print("<a href='../index.html'>home page</a></t><br/>")
    print("<a href='combatant.py'>back to all combatants</a>")
    print("</center>")
    print("</body></html>")

if __name__ == "__main__":
    main()
