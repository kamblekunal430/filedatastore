ortimport json

def add(key,value,ttl,path):
    if path == "":
        path = "datastore.json"
    else:
        path = path+"\datastore.json"
    
    
    try:
        with open(path,'r+') as file:
            if file.tell()<1024*1024*1024:
                if len(key)<=32 and len(value)<=16*1024:
                    data = json.load(file)
                    
                    #print("Data",data)
                    #print("type",type(data))
                    data = dict(data)
                    #print("type",type(data))
                    if key not in data:
                        data[key] = value
                        file.seek(0)
                        json.dump(data,file)
                        print("'key':<value> added to the datastore")
                    else:
                        print("Key already exist in datastore")
                else:
                    print("Key must be of 32 char\nValue must be 16kb")


            else:
                print("Maximum datastore size reached")





    except FileNotFoundError:
        with open(path,'w') as file:
            x = {key:value}
            json.dump(x,file)
            print("'key':<value> added to the datastore")
            
            

    