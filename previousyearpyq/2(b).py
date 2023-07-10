def fAdd(a=2, b=[]):
    b.append(a)
    return b

L1 = fAdd(6)
print(L1)

L2 = fAdd(4)
print(L2)

L3 = fAdd(5)
print(L3)

#In this code, the fAdd function takes two parameters: a with a default value of 2, and b with a default value of an empty list []. Inside the function, the value of a is appended to the list b, and then b is returned.

#Now let's execute the code and examine the output:The first call to fAdd(5) appends 5 to the empty list b, resulting in [5]. The variable L1 stores the returned list, so when we print L1, it displays [5].The second call to fAdd(6) appends 6 to the previously modified list b ([5]), resulting in [5, 6]. The variable L2 stores the returned list, so when we print L2, it displays [5, 6].





#In Python, the append() method is used to add an element to the end of a list. The append() method modifies the original list in-place and does not return a new list. Here's the syntax for using the append() method:

#syntax 
#list_name.append(element)























