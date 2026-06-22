lst=[10,20,30]
tpl=(10,20,30)
lst[0] = 100

#TUPLE CANNOT BE CHANGED AFTER CREATION.

S = "PYTHON"
print(id(S))
S = S + "3"
print(id(S))

d = {1: "one", 2: "one", 3: "two"}
print(d)



r = range(5)
print(r)
print(list(r))
# it will display the range from 0 to 4 

range(1, 10)
range(1, 10, 2)
#1 one will show the does not have the jump value specified hence it will jump by 1 but second one have jump value specified hence it will jump by 2