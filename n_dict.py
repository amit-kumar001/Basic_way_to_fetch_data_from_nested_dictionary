# n_dict is the name of dictionary where 'a' is the (key) and ('b':[1,2,3]) is the value of dictionary n_dict.

n_dict={'a':{'b':[1,2,3]}} # value of 'b' is in list and hence we can go for indexing also
#n_dict is a nested dictionary)

# First way to fetch single value from nested dictionary by using print statement and using keys
print(n_dict['a']['b'][0])

# second way to fetch single value from nested dictionary by using get method defined in dictionary
n=n_dict.get("a").get("b")[0]
print(n)

#third way to fetch single value from nested dictionary by using for loop and values() method defined in dictionary
for b in n_dict.values():
    print(b ['b'][0])

