n_dict={'a':{'b':[1,2,3]}}
print(n_dict)

# First way to fetch single value from nested dictionary by using print statement and using keys
print(n_dict['a']['b'][0])

# second way to fetch single value from nested dictionary by using get method defined in dictionary
n=n_dict.get("a",{}).get("b",{})[0]
print(n)

#third way to fetch single value from nested dictionary by using for loop and values() method defined in dictionary
for a in n_dict.values():
    print(a['b'][0])

