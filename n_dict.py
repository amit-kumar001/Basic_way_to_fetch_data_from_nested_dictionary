n_dict={'a':{'b':[1,2,3]}}
print(n_dict)

print(n_dict['a']['b'][0])

n=n_dict.get("a",{}).get("b",{})[0]
print(n)


for a in n_dict.values():
    print(a['b'][0])

