#Immutability example 
myvariable = 'hello world'
my_init=10
my_float=10.98
my_bool=True
my_string = 'hello world'
my_list = [my_init, my_float, my_bool, myvariable, my_string ]  # this is list in python
print my_list
my_string= 'world'
# even though we have changed the my_string value it is not getting changes in my_list
# because at the time of creating the lilst it was hello world  
print my_list

