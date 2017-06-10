#!/usr/bin/env python3
import cgi
from extra_output import generate_img_tag

def main():
    fields = cgi.FieldStorage()
    default = ""
    #Grabbing all the fields used to generate the page
    #   The user could obviously change the results to whatever he wants
    #   but it'd be kind of silly considering the page is just presenting
    #   information already know in different sections in a different way

    #There's no actual query so the fields don't have to be evaluated just to prevent
    #   a user from doing what he wants
    combatant_1 = fields.getvalue("cmbt1", default)
    combatant_2 = fields.getvalue("cmbt2", default)
    victor = fields.getvalue("victor", default)
    str_time = fields.getvalue("str_time", default)
    length = fields.getvalue("length", default)

    # This is the Head of the HTTP response
    print("Content-type: text/html\n")
    print("<html><center><table><tr>")
    #Has the names has headers above the images
    print("<th>" + combatant_1 + "</th>")
    print("<th></th>")
    print("<th>" + combatant_2 + "</th>")
    print("<tr>")
    print("<td>")
    #Shows the images for the combatants
    generate_img_tag(combatant_1)
    print("</td><td><h2>'  Vs.  '</h2></td><td>")
    generate_img_tag(combatant_2)
    print("</td></tr>")
    print("</table>")
    print("<h1> The victor is...   " + victor + "!</h1>")
    print("<br/> The battle occured on " + str_time)
    print("and lasted for a total of " + length)
    #Links back to the previous page or back to the home page
    print("<br/><a href='battle.py'> back to battles </a>")
    print("<br/><a href='../index.html'>home page</a>")
    print("</center></html>")

if __name__ == "__main__":
    main()
