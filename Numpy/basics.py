import numpy as np

a = [1,2,3]
print(a*2)
t = [q*2 for q in a]
print(t)

print(a+t)

# print(a.shape) gives error list has no shape

a = np.array([1,2,3])
print(a)
b = a*2
print(b)

print(a+b)

print(a.shape)

floatnp = np.float32([1.2,2.3,3.4])
print(floatnp)

# Python list size changes whereas numpy array size remains same 
# np.zeroes(3,int)
#can be used to resrve space

#create array with start va;ues anf end values along with step
arr1 = np.arange(2,6,2)
arr2 = np.arange(6)
arr3 = np.arange(2,5)

# can handle floats as wwll
print(np.arange(1.2,3.2,0.5))
print(arr1,arr2,arr3)

# np.random kind of functions to generate random arrays for testing


# imp ways of vector indexing
print(".........................")
myarray = np.arange(8)

print(myarray[0])
print(myarray[1:3])
print(myarray[:2])
print(myarray[3:])
print(myarray[-2:])
print(myarray[[0,3]])

# all these can be  read as well as values can be edited

a = [1,2,3]
print([q>2 for q in a])

# print(a[a>2])         #error

b = np.arange(5)
print(b[b>2])

t =np.where(b>=3)[0] #check net why [0] is used it returns a object 
print(t)


test = np.arange(7)
final = np.float64(test/7)

test[0] = 6
# passes a reference i f u want to make a copy u have to use copy function 
print(final)

# some arithmetic operations 
print(
np.sqrt(test),
np.exp(test),
np.log(test)
)

# np.dot() acn be used to take dot product of 2 vectors
# np.cross()

print(np.int32(np.floor(np.sqrt(test))))
# ceil round
# max min also works


# sorting an np array

t = np.array([2,3,1])
sorted = np.sort(t)
print(sorted,t)
t.sort()
print(t)



print(0.1+0.2 == 0.3)
print(np.allclose(0.1+0.2))







