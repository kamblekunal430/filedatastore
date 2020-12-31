from filedatastore import datastore
import os

def help():
    usage = '''
    Operations:-

    create(key,value,time_to_live(optional))
    read(key)
    delete(key)
    '''
    print(usage)

def create(key,value,ttl=0,path=""):
    datastore.add(key,value,ttl,path)




print("Do you want to specify datastore location? (Y/N)")
if input().lower() == 'y':
    print("Enter the path for datastore")
    path = input()
    print("Datastore path initialized")

else:
    path=""

help()



    