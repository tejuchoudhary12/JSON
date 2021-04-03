import json
data={"name": "David",
     "class":"I",
     "age": 6  
 }
my_file=json.dumps(data)
print(type(my_file))
print(my_file)