dict1={"Amol":65.1,"mahesh":70.1,"suresh":90.2,"Omkar":65.1}

print(dict1)     #{'Amol': 65.1, 'mahesh': 70.1, 'suresh': 90.2, 'Omkar': 65.1}

print(len(dict1))      #4

print("----get value of specific key-----")
print(dict1["suresh"])            #90.2

print("----add new k-v pair-----")
dict1["Arjun"]=70.2          #{'Amol': 65.1, 'mahesh': 70.1, 'suresh': 90.2, 'Omkar': 65.1, 'Arjun': 70.2}
print(dict1)

print("-----update/modify value of specific key-----")
dict1["mahesh"]=77.1
print(dict1)

print("-----remove/delete specific key-value -----")
dict1.pop("suresh")           #{'Amol': 65.1, 'mahesh': 77.1, 'Omkar': 65.1, 'Arjun': 70.2}
print(dict1)

print("-----remove last inserted item(k-v) -----")
dict1.popitem()              #{'Amol': 65.1, 'mahesh': 77.1, 'Omkar': 65.1}
print(dict1)

print("-----check key exist in dict -----")
print("Amol" in dict1)     # True


