# import json 
# data={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4
#     }
# my_file=json.dumps(data,sort_keys=True)
# print(type(data))
# print(my_file)

import json 
data={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
dict={}
a=sorted(data.keys())
for i in a :
    dict[i]=data[i]
jsonDic=json.dumps(dict)
print(jsonDic)
print(type(jsonDic))