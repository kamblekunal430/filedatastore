# filedatastore
A file based key value data store in python that support the basic CRD (create, read, and deleter) operations.
It can be used as a library to instiantiate and work

The data store will support the following function requirements :

It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
A new key-value pair can be added to the data store using the Create operation. 
The key is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.
A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
A Delete operation can be performed by providing the key.
Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. 
Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
The file size never exceeds 1GB.

