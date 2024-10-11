def get_file_name():
    exists = False
    name = str(input("Type a file name: "))
    if exists == False:
        name = str(input("Type a file name: "))
        try:
            file = open(name)
        except:
            exists = False
        else:
            exists = True
            return name
            
