import json

#Reading JSON from a file using Python
#1. Using json.load() 

with open("samplejson.json","r") as f:
    data = json.load(f)


for d in data:
    for key,value in d.items():
        print(key , " : ",value)

#2. Using json.loads()

json_str = '{"name":"SSK","batch No": 268094,"CGPA":9.0,"Dept":"Computer Science"}'

data_str = json.loads(json_str)
print(data_str)

# Using json.dumps() 

json_str2 = {"name":"SSK","batch No": 268094,"CGPA":9.0,"Dept":"Computer Science"}
json_str3 = {"name":"S Santhosh Kumar","batch No": 268000,"CGPA":8.60,"Dept":"Artificial Intelligence and Data Science"}
json_strf= [json_str2,json_str3]

data_str2 =  json.dumps(json_strf,indent=4)

with open("samplejson.json","w") as fw:
    fw.write(data_str2)

# Using json.dump() 

json_str3 = {"name":"S Santhosh Kumar","batch No": 268000,"CGPA":8.60,"Dept":"Artificial Intelligence and Data Science"}

with open("samplejson2.json","w") as fw1:
    json.dump(json_str3,fw1,indent=4)