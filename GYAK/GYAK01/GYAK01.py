#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

#1
def contains_odd(input_list):
    for xc in input_list:
        if xc%2 != 0:
            return True
    return False

#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

#2
def is_odd(input_list):
    res = list(map(lambda x: x%2!=0, input_list))
#    for xc in input_list:
 #       if xc%2 != 0:
  #          res.append(True)
   #     else:
    #        res.append(False)
    return res

#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

#3
def element_wise_sum(input_list_1, input_list_2):
    res = list(map(lambda x,y: x+y, input_list_1, input_list_2))
    if len(input_list_1)>len(input_list_2):
        cnt=len(input_list_2)
        while cnt<len(input_list_1):
            res.append(input_list_1[cnt])
            cnt+=1
    elif len(input_list_2)>len(input_list_1):
        cnt=len(input_list_1)
        while cnt<len(input_list_2):
            res.append(input_list_2[cnt])
            cnt+=1
    return res

#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

#4
def dict_to_list(input_dict):
    res = [(k,v) for k,v in input_dict.items()]
    #for xc in input_dict:
    #    res.append(tuple(xc.key, xc.value))
    return res