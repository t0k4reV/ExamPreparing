login = "' union select 1, 2, 3, 4, 5 --"

connection.execute(f""" select * 
                   from users 
                   where login = '{login}'
                   and password = '{password}'""")
