"""
By : goishen
Date : 08-14-20

"""


import database

MENU_TEXT = """
1.  Add a new client
2.  See all clients
3.  Search by name
4.  Search by zipcode
5.  Delete from database
6.  Quit
"""

def Main():
    connection = database.connect()
    database.create_tables(connection)
    while (main_menu_input := input(MENU_TEXT)) != "6":
        if main_menu_input == "1":
            name = input("Name : ")
            address = input("Address : ")
            city = input("City : ")
            state_us = input("State : ")
            zipcode = (input("Zipcode : "))
            database.add_handyman(connection, name, address, city, state_us, zipcode)
        elif main_menu_input == "2":
            all_db = database.get_all_handyman(connection)
            for i in all_db:
                print(f"ID# :\tNames and Addresses")
                print("----------------------------------------------------------")
                print(f"{i[0]}\tName : {i[1]}\n\tAddress: {i[2]}\n\tCity : {i[3]}\t\tState : {i[4]}\tZip : {i[5]}\n\n")
        elif main_menu_input == "3":
            pattern = input("Search by name : ")
            names_search = database.search_handyman_by_name(connection, pattern)
            if names_search != []:
                print("\n\nID# :\tName and Addresses")
                print("---------------------------------------------------------")  
                for i in names_search:
                    print(f"{i[0]}\t{i[1]}\n\t{i[2]}\n\t{i[3]} {i[4]}, {i[5]}\n\n")                
            else:
                print("\n\nNothing found!\n\n")
        elif main_menu_input == "4":
            zipcode = (input("Search by zipcode : "))
            names_search = database.search_handyman_by_zip(connection, zipcode)
            if names_search != []:            
                print("\n\nID# : \tNames and Addresses")
                print("---------------------------------------------------------")
                for i in names_search:
                    print(f"{i[0]}\t{i[1]}\n\t{i[2]}\n\t{i[3]} {i[4]}, {i[5]}\n\n")
            else:
                print("\n\nNothing found!\n\n")
        elif main_menu_input == "5":
            id_ = input("ID number to delete : ")
            database.del_by_id(connection, id_)
            print("Deleted ID # ", id_)

if __name__ == "__main__":
    Main()

