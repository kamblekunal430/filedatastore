

# Function to set the path of datastore
def set(path=""):
    with open("const.txt",'w') as file:
        if path=="":
            file.write("datastore.json")
        else:
            file.write(path+"\datastore.json")
            

# Function to get the datastore path
def path():
    with open("const.txt") as file:
       # print(file.read())
        return file.read()