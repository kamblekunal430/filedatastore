from filedatastore import datastore
from filedatastore import constant
import os



# Function to display the operation that can be performed.
def help():
    datastore.help()

# Function to create/add key-value to the datastore
def create(key,value,ttl=0):
    datastore.add(key,value,int(ttl))

def read(key):
    datastore.read_data(key)




# Driver code

print("Do you want to specify datastore location? (Y/N)")
if input().lower() == 'y':
    print("Enter the path for datastore")
    path = input()
    constant.set(path)
    #print("init",constant.path())
    print("Datastore path initialized")
else:
    constant.set()


datastore.help() # To display the help menu



    