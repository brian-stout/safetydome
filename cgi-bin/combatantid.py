#!/usr/bin/env python3
import cgi
from queries import select_combatant, get_record
from extra_output import generate_img_tag

def main():

    fields = cgi.FieldStorage()
    default = ""
    combatantId = fields.getvalue("cid", default)

    row = select_combatant(combatantId)
    record = get_record(combatantId)

    # This is the Head of the HTTP response
    print("Content-type: text/html\n")
    #This begins the Body of hte HTTP Response
    print("<html><head><title>WSDL : " + row[1] + "</title>")
    print("<style> table, th, td { border: 1px solid black; }</style></head>")
    print("<body><center>")
    generate_img_tag(row[1])
    print("<table style='width:30%'>")

    print("<tr>")
    print("<th>" + row[1] + "</th>")
    print("<th> ID: " + str(row[0]) + "</th>")
    print("</tr>")

    print("<tr>")
    print("<td style='text-align:justify'>species: </td>")
    print("<td>" + row[2] + "</td>")
    print("</tr>")

    print("<tr>")
    print("<td style='text-align:justify'>type:</td>")
    print("<td>" + row[3] + "</td>")
    print("</tr>")

    print("<tr>")
    print("<td style='text-align:justify'>attack:</td>")
    print("<td>" + str(row[4]) + "</td>")
    print("</tr>")

    print("<tr>")
    print("<td style='text-align:justify'>defense:</td>")
    print("<td>" + str(row[5]) + "</td>")
    print("</tr>")

    print("<tr>")
    print("<td style='text-align:justify'>hp:</td>")
    print("<td>" + str(row[6]) + "</td>")
    print("</tr>")

    print("<tr>")
    print("<td style='text-align:justify'>wins:</td>")
    print("<td>" + str(record[0]) + "</td>")
    print("</tr>")

    print("<tr>")
    print("<td style='text-align:justify'>total battles:</td>")
    print("<td>" + str(record[1]) + "</td>")
    print("</tr>")

    print("<tr>")
    print("<td style='text-align:justify'>w/l ratio:</td>")
    if (record[1] > 0):
        print("<td>" + str(record[0] / record[1]) + "</td>")
    else:
        print("<td> No value </td>")
    print("</tr>")
    
    print("</table></center>")
    print("</body></html>")

if __name__ == "__main__":
    main()

