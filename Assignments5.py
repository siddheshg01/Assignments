b =bytes([65,66,67])
print(b)
#bytes([65,66,67]) converts each integer  into a byte and store which Python displays as b'ABC'

ba = bytearray([65,66,67])
ba[0] = 97
print(ba)
#bytearray allows changing its contents after creation, so 97 is valid, whereas bytes objects cannot be modified.

x = None
print(type(x))
print(x == False)
#None and False are both falsy values, but they are different types (NoneType and bool), so None == False evaluates to False.
s = {10,20,30,10,20}
print(s)
#because 10 and 20 are repeated in the set hence they are displayed once in the output.