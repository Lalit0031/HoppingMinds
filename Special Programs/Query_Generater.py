# create table
def Query(): 
    create_table = input("Enter table name : ")
    y = ""
    data_types = {1:"Varchar(20)",2:"Int(20)",3:"Float(20)",4:"Bool(10)"}
    add_column = 0
    while True:
        column_name = input("Enter column name : ") 
        for k,v in data_types.items():
            print(f"Press {k} for {v}")
        data_type = int(input("Enter Data type of column : "))
        dd = ""
        while not any(i == data_type for i in data_types.keys()):
            print("Not a valid data type enter again ")
            data_type = int(input("Enter valid Data type : "))
        else:
            dd = data_types[data_type]

        y += column_name+ " " + dd + ","
        print(y)
        c = input("Do you want more column (y/n): ")
        if c.lower() == 'n':
            break
            
        print("------------------------------------------------------------------------------------------------")
    print('***************************************************************************************************')
    z = "CREATE TABLE {} ({});".format(create_table,y[:len(y)-1])     
    print(z)
    
