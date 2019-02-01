# Basic_way_to_fetch_data_from_nested_dictionary
## Key features
<ol>
  <li>We are having a nested dictionary with it's value in list </li>
  <li>Fetching single value  from nested dictionary using different ways</li>
  <li>First way :- To find single value using print statement,keys (fetching values using keys) and element of particular index in list</li>
  <li>Second way:- By using <strong> get() method</strong> (in-built methods of dictionary)
, we find single value (values of nested dictionary is inside a list) using indexing </li>
  <li>Third way:- Fetching value using dictionary method <strong>dictionary.values()</strong> (in-built methods of dictionary)
  </ol>
  
  ## Implementing ways with code
  
  ### First Way
  ```
  n_dict={'a':{'b':[1,2,3]}}
  print(n_dict)

  print(n_dict['a']['b'][0])
  ```
  ### Second Way
  ```
  n_dict={'a':{'b':[1,2,3]}}
  print(n_dict)
  n=n_dict.get("a",{}).get("b",{})[0]
  print(n)
  ```
  ### Third Way
  ```
  n_dict={'a':{'b':[1,2,3]}}
  print(n_dict)
  for a in n_dict.values():
    print(a['b'][0])  
  ```
  ## How to run this file
  Since this is a python file, hence it can be run using following command

  ```
  python playing_with_python.py
  python3 playing_with_python.py
  ```

    
    
