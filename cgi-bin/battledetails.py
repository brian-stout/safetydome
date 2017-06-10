#!/usr/bin/env python3
import cgi

def main():
    fields = cgi.FieldStorage()
    default = ""
    combatant_1 = fields.getvalue("cmbt1", default)
    combatant_2 = fields.getvalue("cmbt2", default)
    victor = fields.getvalue("victor", default)
    str_time = fields.getvalue("str_time", default)
    length = fields.getvalue("length", default)

    # This is the Head of the HTTP response
    print("Content-type: text/html\n")
    print("<html>")
    print(combatant_1)
    print(combatant_2)
    print(victor)
    print(str_time)
    print(length)
    print("</html>")

if __name__ == "__main__":
    main()
