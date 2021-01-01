import json
import time
from filedatastore import constant


# Function to display the operation that can be performed on datastore.
def help(): 
    usage = '''
    Operations:-

    create(key,value,time_to_live(optional))
    read(key)
    delete(key)

    '''
    print(usage)

# Function to add key-value to the datastore
def add(key,value,ttl):
    # Getting the datastore path
    filepath = constant.path()
    try:
        with open(filepath,'r+') as file:

            # Checking the max size of datastore is reached or not
            if file.tell() < (1024*1024*1024) - 16:

                # Checking if the key is less than 32 char and value is of 16kb
                if len(key)<=32 and len(value)<=16*1024:
                    data = json.load(file)
                    
                    #print("Data",data)
                    #print("type",type(data))
                    data = dict(data)
                    #print("type",type(data))

                    
                    if key not in data:
                        # adding the key value to the datastore if the key does not exist 
                        data[key] = [value,time.time()+ttl if ttl else ttl] # Also setting the time-to-live
                        
                        # writing data to datastore
                        file.seek(0)
                        json.dump(data,file)
                        print("'key':<value> added to the datastore")

                    else:
                        print("Key already exist in datastore")

                else:
                    print("Key must be of 32 char\nValue must be 16kb")


            else:
                print("Maximum datastore size reached")


    # if the file not found
    except FileNotFoundError:

        # creating the file and adding the key-value pair
        with open(filepath,'w') as file:
            x = {key:[value,time.time()+ttl if ttl else ttl]} # also setting the time-to-live

            # writing data to the datastore
            json.dump(x,file)
            print("'key':<value> added to the datastore")
            

# Function to read the VALUE of the KEY form the datastore
def read_data(key):
    # Getting the datastore path
    filepath = constant.path()
    
    try:
        # opening datastore to read and write
        with open(filepath,'r+') as file:

            # reading data from the datastore
            data = json.load(file)

            data = dict(data)

            # checking if the key exist is data
            if key in data:
                if data[key][1] > 0: # checking if the key has time-to-live
                    if data[key][1] > time.time(): # checking if the time-to-live has completed
                        print("Value:-\n",data[key][0])
                    else:
                        delete_data(key)
                else:
                    print("Value:-\n",data[key][0])
            else:
                print("Key is invalid or has expired!")

    
    except FileNotFoundError: # if unable to read the datastore
        print("Unable to read the datastore! Create a datastore")
        help()


#function to delete the key-value form the datastore
def delete_data(key):
    # Getting the datastore path
    filepath = constant.path()
    try:
        # accessing the datastore to read and write
        with open(filepath,'r+') as file:

            # loading the data from the datastore
            data = json.load(file)

            data = dict(data)

            if key in data: # checking if the key exist in datastore
                if data[key][1] > 0: # checking if the key has time to live property
                    if data[key][1] > time.time(): # checking if the time to live is reached
                        data.pop(key)
                        print("'key':<value> successfully deleted")
                    else:
                        data.pop(key)
                        print("The key has expired!")
                else:
                    data.pop(key)
                    print("'key':<value> successfully deleted")
            else:
                print("Key is invalid or has expired!")
            
            # writing data to the datastore
        with open(filepath,'w') as file:    
            json.dump(data,file)

    except FileNotFoundError:
        print("Unable to read the datastore! Create a datastore")
        help()

    

            

    