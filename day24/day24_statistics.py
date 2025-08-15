import numpy as np
py_list = [1,2,3,4,5]
print(type(py_list))
print(py_list)

two_dimension_list = [[0,1,2],[3,4,5],[6,7,8]]
print(two_dimension_list)

numpy_array_from_list = np.array(py_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

#creating float numpy array
numpy_array_from_list2 = np.array(py_list,dtype=float)
print(numpy_array_from_list2)

#creating boolean numpy array
numpy_bool_array = np.array([0,1,-1,0,0,1],dtype=bool)
print(numpy_bool_array)

#creating multidimensional array using numpy
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimension_list)
print(numpy_two_dimensional_list)

#creating numpy array to list
np_to_list = numpy_array_from_list.tolist()
print(np_to_list)

#creating numpy array from tuple
py_tup = (1,2,3,4,5)
numpy_array_from_tuple = np.array(py_tup)
print(type(numpy_array_from_tuple))
print('numpy array from tuple:', numpy_array_from_tuple)

#shape of numpy array 
nums = np.array([1, 2, 3, 4, 5])
print("shape of nums :",nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ',
numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(three_by_four_array.shape)

#data type of numpy array
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

#size of numpy array
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8],[4,5,5],[6,6,8]])

print(numpy_array_from_list.size)
print(two_dimensional_list.size)

#mathmatical operations  using numpy
#addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
add_array = numpy_array_from_list + 10
print(add_array)

#substraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
sub_array = numpy_array_from_list - 10
print(sub_array)

#multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
mul_array = numpy_array_from_list * 10
print(mul_array)

#division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
div_array = numpy_array_from_list /10
print(div_array)

#modulas
print('original array: ', numpy_array_from_list)
mod_array = numpy_array_from_list %3
print(mod_array)

#floor division
print('original array: ', numpy_array_from_list)
floor_array = numpy_array_from_list // 10
print(floor_array)

#exponatial
print('original array: ', numpy_array_from_list)
exp_array = numpy_array_from_list **2
print(exp_array)

#Checking data types
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

#Converting types
#1.int to float
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
print(numpy_int_arr)

#2. Float to Int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)

#3. Int ot boolean
print(np.array([-3, -2, 0, 1,2,3], dtype='bool'))

#4. Int to str
strnmu = numpy_int_arr.astype('int').astype('str')
print(strnmu)

#multidimenstional array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

#getting items from numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print(first_row)
print(second_row)
print(third_row)

first_column = two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('first column',first_column)
print('second column',second_column)
print('third column',third_column)

#Slicing Numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

#How to reverse the rows and the whole array?
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
reverse = two_dimension_array[::-1,::-1]
print(reverse)

#How to represent missing values ?
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

# Numpy Zeroes
num_zero = np.zeros((3,3),dtype=int ,order='c' )
print(num_zero)

#numpy ones
num_one = np.ones((3,3),dtype=int , order='C')
print(num_one)
print(num_one*2)

#reshape
first_shape = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

#flattened
flattened = reshaped.flatten()
print(flattened)

#horizntal stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])

print(np_list_one + np_list_two)
print('horizontal append',np.hstack((np_list_one,np_list_two)))

#vertical stack 
print('vertical append:',np.vstack((np_list_one,np_list_two)))

#Generating Random Numbers
ran = np.random.random(3)
print(ran)

## Generating a random integers between 0 and 10
ranint = np.random.randint(0,11)
print(ranint)

## Generating a random integers between 2 and 11, and creating a one row array
ranint = np.random.randint(2,11,size=4)

# Generating a random integers between 0 and 10
random_int = np.random.randint(2,10, size=(3,3))
print(random_int)

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(39, 25,50)
print(normal_array)

#Numpy and Statistics
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)

#Matrix in numpy
matrix = np.matrix(np.ones((3,3),dtype=int))
print(matrix)
np.asarray(matrix)[2]=23
print(matrix)

# Similar to range arange numpy.arange(start, stop, step)
even = np.arange(0,100,2)
print(even)

# numpy.linspace()
print(np.linspace(1,5,num=10))
# not to include the last value in the interval
print(np.linspace(1,5,num=5,endpoint=False))

# to check the size of an array
x = np.array([1,2,3],dtype=np.complex128)
print(x)
print(x.itemsize)

## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
#print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

print(two_dimension_array)
print('column with minimum :',np.amin(two_dimension_array,axis=0))
print('column with maximum : ',np.amax(two_dimension_array,axis=0))
print("===row===")
print("row with minimum",np.amin(two_dimension_array,axis=1))
print("row with maximum",np.amax(two_dimension_array,axis=1))

#How to create repeating sequences?
a = [1,2,3]
# Repeat whole of 'a' two times
print('tittle = ',np.tile(a,2))
#Repeat each element of 'a' two times
print("repeat = ",np.repeat(a,2))

np_normal_dis = np.random.normal(5, 0.5, 1000)
plt.hist(np_normal_dis, color="grey", bins=205)
plt.show()

#linear algebra
a =[1,2,3]
b= [4,5,6]
print(np.dot(a,b))

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

mu = 28
sigma = 15
samples = 100000
x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
