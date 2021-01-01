from filedatastore import datastore
from filedatastore import constant
import os



# Function to display the operation that can be performed.
def help():
    datastore.help()

# Function to create/add key-value to the datastore
def create(key,value,ttl=0):
    datastore.add(key,value,int(ttl))

# Function to read the key-value from the datastore
def read(key):
    datastore.read_data(key)

# Function to delete the key form the datastore
def delete(key):
    datastore.delete_data(key)




# Driver code

print("Do you want to specify datastore location? (Y/N)")
if input().lower() == 'y':
    print("Enter the path for datastore")
    path = input()

    # setting the path of datastore
    constant.set(path)
    #print("init",constant.path())
    print("Datastore path initialized")

else:
    # setting default path of the datastore
    constant.set()

datastore.help() # To display the help menu