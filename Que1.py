import json
Data='{"Name":"Ram", "class":"v","age":9}'
my_file=json.loads(Data)
print(type(my_file))
print(my_file)