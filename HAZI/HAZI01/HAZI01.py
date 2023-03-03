# %%
#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

# %%
def subset(input_list, start_index, end_index):
    res = input_list[start_index, end_index+1]
#    while start_index <= end_index:
#        res.append(input_list[start_index])
#        start_index+=1
    return res

# %%
#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

# %%
def every_nth(input_list,step_size):
    res = input_list[step_size-1::step_size]
#    cnt= step_size-1
#    while cnt <= input_list.len():
#        res.append(cnt)
#        cnt+= step_size
    return res 

# %%
#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

# %%
def unique(input_list):
    return len(set(input_list))==len(input_list)

# %%
#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list

# %%
def flatten(input_list):
    res = [x for li in input_list for x in li]
    return res 

# %%
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args


# %%
def merge_lists(*args):
    res = []
    for xc in args:
        res.extend(xc)
    return res

# %%
#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

# %%
def reverse_tuples(input_list):
    res = list(map(lambda x: tuple(x[1],x[0]), input_list))
    return res

# %%
#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list

# %%
def remove_tuplicates(input_list):
    return list(set(input_list))

# %%
#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

# %%
def transpose(input_list):
    res = [list(x) for x in zip(*input_list)]
    return res

# %%
#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size

# %%
def split_into_chunks(input_list,chunk_size):
    xc = [x for li in input_list for x in li]
    return([xc[x:x+chunk_size] for x in range(0,len(xc),chunk_size)])

# %%
#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

# %%
def merge_dicts(*dict):
    res = {}
    for xc in dict:
        res.update(xc)
    return res

# %%
#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list

# %%
def by_parity(input_list):
    ev=[]
    o=[]
    for x in input_list:
        if x%2 == 0:
            ev.append(x)
        else:
            o.append(x)
    res={"even":ev, "odd":o}
    return res

# %%
#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

# %%
def mean_key_value(input_dict):
    for key, value in input_dict.items():
        if value!=0:
            input_dict[key]=sum(value, 0.0) /len(value)
        else:
            input_dict[key]=0
    return input_dict        

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


