import json 
filename='data.txt'
dict1={}
with open(filename) as a: 
  
    for i in a: 
        key, value = i.strip().split(None, 1) 
        dict1[key] = value.strip() 
 
out_file = open("data.txt", "w") 
json.dump(dict1, out_file, indent = 4) 
out_file.close() 