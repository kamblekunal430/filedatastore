# Function to set the path of datastore
def set(path=""):

    # adding the path to the file
    with open("const.txt",'w') as file:

        if path=="":
            file.write("datastore.json") # creating a default path if not entered by user
        else:
            file.write(path+"\datastore.json") # writing the path given by the user
            

# Function to get the datastore path
def path():
    with open("const.txt") as file:
       # print(file.read())
        return file.read() 