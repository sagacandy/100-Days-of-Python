dic = {
    "name": "saga",
    "class": "devops",
    "address": "india"
}
print(dic)
print(dic["class"])
print(dic.keys())

print(dic.values())
for key in dic.keys():
    print(f"The value of key {key} is {dic[key]}")
print(dic.items())
