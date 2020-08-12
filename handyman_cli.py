import database

MENU_TEXT = """
1.  Add a new client
2.  See all clients
3.  Search by name
4.  Search by zipcode
5.  Quit
"""

def Main():
    connection = database.connect()
    database.create_tables(connection)

    while (main_menu_input := input(MENU_TEXT)) != "5":
        if main_menu_input == "1":
            name = input("Name : ")
            address = input("Address : ")
            city = input("City : ")
            state_us = input("State : ")
            try:
                zipcode = int(input("Zipcode : "))
            except ValueError as e:
                print("Please enter a numeric zipcode!")
            database.add_handyman(connection, name, address, city, state_us, zipcode)
        elif main_menu_input == "2":
            all_db = database.get_all_handyman(connection)
            for i in all_db:
                print("----------------------------------------------------------")
                print(f"Name : {i[1]}\nAddress: {i[2]} \nCity : {i[3]}\t\tState : {i[4]} \tZip : {i[5]}")
        elif main_menu_input == "3":
            name = input("Search by name : ")
            names_search = database.get_handyman_by_name(connection, name)
            print("ID# :\tName and Addresses")
            print("---------------------------------------------------------")
            for i in names_search:
                if i in names_search:
                    print(f"{i[0]}\t{i[1]}\n\t{i[2]}\n\t{i[3]}\
                          {i[4]}, {i[5]}\n\n")                
                else:
                    print("Nothing found!")
        elif main_menu_input == "4":
            zipcode = input("Search by zipcode : ")
            names_search = database.get_handyman_by_zip(connection, zipcode)
            print("ID# : \tNames and Addresses")
            print("---------------------------------------------------------")
            for i in names_search:
                if i in names_search:
                    print(f"{i[0]}\t{i[1]}\n\t{i[2]}\n\t{i[3]} {i[4]}, {i[5]}\n\n")
                else:
                    print("Nothing found!")

if __name__ == "__main__":
    Main()

