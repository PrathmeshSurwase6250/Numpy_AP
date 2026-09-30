# 🟢 Level 1 — NumPy Basics
# 1. Create an array
import numpy as np
# Create a NumPy array containing:

# 10, 20, 30, 40, 50
numpy = np.arange(10,51,10)

# Print:
# array
print(numpy)
# datatype
print(numpy.dtype)
# number of elements
print(numpy.size)
# size
print(numpy.itemsize)
# dimensions
print(numpy.ndim)
# shape
print(numpy.shape)
# 2. Create arrays using arange()

# Create:

# [1, 2, 3, ..., 20]
num1 = np.arange(1,21)

print(num1)
# Then create:
# [2, 4, 6, ..., 20]
num1 = num1[num1 % 2 ==0]
print(num1) 
# 3. Create an array of zeros

# Create a 3 × 4 array containing only zeros.
zeros = np.zeros(12).reshape(3,4)
print(zeros)
# 4. Create an array of ones

# Create a 5 × 5 array containing only ones.
ones = np.ones(25).reshape(5,5)
print(ones)
# 5. Create an identity matrix

# Create a 4 × 4 identity matrix.
identity = np.identity(4)
print(identity)
# 6. Reshape

# Create numbers from 1 to 24 and reshape them into:
num2 = np.arange(1,25).reshape(4,6)
# 4 × 6

print(num2)
# Then reshape the same data into:

# 2 × 3 × 4
num2 = num2.reshape(2,3,4)
print(num2)
# 7. Flatten

# Given:

# a = np.arange(1, 13).reshape(3, 4)
a = np.arange(1, 13).reshape(3, 4)
# Convert it into:

# [1 2 3 ... 12]
a = np.ravel(a)
print(a)

# 8. Transpose

# Given:

# a = np.arange(1, 13).reshape(3, 4)
a = np.arange(1, 13).reshape(3, 4)

# Find its transpose.
print(a.T)

# 9. Generate evenly spaced numbers

# Generate 50 numbers between -10 and 10 using linspace().
linspaces = np.linspace(-10 ,10 ,50)
print(linspaces)
# 10. Random numbers

# Generate:

# 10 random integers between 1 and 100
random = np.random.randint(1,101,10)
print(random)
# a 3 × 3 matrix of random integers
a = np.arange(9).reshape(3,3)
print(a)
# 10 random floating-point numbers between 0 and 1
random10 = np.random.random(10)
print(random10)
# 🟢 Level 2 — Indexing & Slicing
# 11. Basic indexing

# Given:

# a = np.arange(1, 21)
a = np.arange(1, 21)
# Find:

# first element
print(a[0])
# last element
print(a[-1])
# fifth element
print(a[4])
# element at index 10
print(a[10])
# last 5 elements
print(a[14:])
# 12. Slicing

# Given:

# a = np.arange(1, 21)
a = np.arange(1, 21)
# Extract:

# 1 to 10
print(a[0:11])
# 5 to 15
print(a[4:16])
# even-indexed elements
print(a[::2])
# elements in reverse order
print(a[::-1])
print(np.flip(a))  #inbuilt python function
# 13. 2D indexing

# Given:

# a = np.arange(1, 17).reshape(4, 4)
a = np.arange(1, 17).reshape(4, 4)
# Find:
print(a)
# first row
print(a[0])
# last row
print(a[-1])
# first column
print(a[:,0])
# last column
print(a[:,-1])
# element at row 2, column 3
print(a[1,2])
# 14. Extract a submatrix
a = np.arange(1, 17).reshape(4, 4)
# From:

# 1  2  3  4
# 5  6  7  8
# 9 10 11 12
# 13 14 15 16

# extract:

# 6  7
# 10 11
print(a[1:3 ,1:3])
# 15. Reverse rows

# Given a 4 × 4 matrix, reverse the order of its rows.
print(a[::,::-1])
# 16. Reverse columns

# Reverse the order of columns in a matrix.
print(a[::-1,::])
# 🟡 Level 3 — Fancy & Boolean Indexing
# 17. Fancy indexing

# Given:

# a = np.arange(1, 21)
a = np.arange(1, 21)
# Extract elements at indexes:

# 0, 3, 7, 10, 15
print(a[[0,3,7,10,15]])
# 18. Select multiple rows

# Given:

# a = np.arange(1, 26).reshape(5, 5)
a = np.arange(1, 26).reshape(5, 5)
# Extract rows:
print(a)
# 0, 2, 4
print(a[::2])
# 19. Select multiple columns

# From the same matrix, extract columns:

# 1, 3, 4
print(a[[1,3,4]])
# 20. Even numbers

# Given:

# a = np.arange(1, 101)
a = np.arange(1, 101)
# extract all even numbers using Boolean indexing.
print(a[a % 2 == 0])
# 21. Numbers greater than 50

# Extract all numbers greater than 50.
print(a[a>50])
# 22. Numbers between 30 and 70

# Extract numbers satisfying:

# 30 <= x <= 70
print(a[(a>30) & (a<70)])
# 23. Divisible by 3 and 5

# From 1–100, find numbers divisible by both 3 and 5.
print(a[(a%3==0)| (a%5==0)])
# 24. Replace values

# Given:

# a = np.arange(1, 21)
a = np.arange(1, 21)
# replace every number greater than 10 with 0.
a[a>10] = 0
print(a)
# Expected:

# [1 2 3 4 5 6 7 8 9 10 0 0 0 0 0 0 0 0 0 0]
# 25. Clip values

# Given an array containing values from -20 to 20, replace:
a = np.arange(-20,21)
print(a)
# values below -5 → -5
a[a < -5] = -5
print(a)
# values above 5 → 5
a [a > 5] = 5
print(a)
# 🟡 Level 4 — Mathematical Operations
# 26. Array arithmetic

# Given:

# a = np.array([10, 20, 30, 40])
# b = np.array([1, 2, 3, 4])
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
# Calculate:

# a + b
c = a + b
print(c)
# a - b
c = a - b
print(c)
# a * b
c = a * b
print(c)
# a / b
c = a / b
print(c)
# a ** 2
c = a ** b
print(c)
# 27. Mathematical functions

# Given:

# a = np.array([0, 1, 4, 9, 16, 25])
a = np.array([0, 1, 4, 9, 16, 25])
# calculate:

# square root
print("Square root:", np.sqrt(a))
# square
print(np.square(a))
# exponential
print(np.exp(a))
# logarithm
print(np.log(a))

# using NumPy functions.

# 28. Find min/max

# Generate 20 random numbers and find:
a =  np.random.randint(1,101,20)

# minimum
print(np.min(a))
# maximum
print(np.max(a))
# index of minimum
print(np.argmin(a))

# index of maximum
print(np.argmax(a))
print()
# 29. Sum and product

# Given:

# a = np.arange(1, 11)
a = np.arange(1, 11)
# calculate:

# sum
print(np.sum(a))
# product
print(np.prod(a))
# mean
print(np.mean(a))
# median
print(np.median(a))
# 30. Row-wise statistics

# Given:

# a = np.arange(1, 13).reshape(3, 4)
a = np.arange(1, 13).reshape(3, 4)
# Find the:

# sum of each row
print(a.sum(axis=1))
# mean of each row
print(a.mean(axis=1))

# maximum of each row
print(np.max(a,axis=1))
# minimum of each row
print(np.min(a,axis=1))
# 31. Column-wise statistics

# Using the same matrix, calculate the same statistics column-wise.

# This is important for understanding:

# axis=0
# axis=1
# 🟡 Level 5 — Broadcasting
# 32. Scalar broadcasting

# Given:

# a = np.arange(1, 6)
a = np.arange(1, 6)
# Add 10 to every element without using a loop.
b = np.array([10])
c  = a+b
print(c)
# 33. Vector broadcasting

# Given:

# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ])


# b = np.array([10, 20, 30])
b = np.array([10, 20, 30])
# Add b to every row.
c = a+b
print(c)
# 34. Broadcasting subtraction

# Given:

# 10 20 30
# 40 50 60
# 70 80 90
a = np.arange(10,91,10).reshape(3,3)
# subtract:

# 1 2 3
b = np.array([1, 2, 3])
# from every row.
c = a - b 
print(c)
# 35. Broadcasting challenge

# Can you multiply this without loops?

# a = np.arange(1, 13).reshape(4, 3)
a = np.arange(1, 13).reshape(4, 3)
# b = np.array([10, 20, 30])
b = np.array([10, 20, 30])
print(a*b)
# 36. Broadcasting compatibility

# Determine whether these operations work:

# (3, 4) + (4,) yes it will work because broadcasting second rule it follow that in another demension is only for 4 -> (1,4) and it upscale to (3,4)
# (3, 4) + (3,) no
# (3, 1) + (1, 4) yes
# (2, 3, 4) + (3, 4) yes

# Don't just run them—explain why.

# 🟠 Level 6 — Statistics
# 37. Mean
a = np.random.randint(1,101,20)
# Calculate the mean manually using a loop and then compare it with:
population = 0
count = 0
for i in a :
    population = population + i
    count = count+1
    
mean = population / count
print("Mean:", mean)
# np.mean()
print(np.mean(a))
# 38. Median

# Given:

# 10, 20, 30, 40, 100
a = np.array([10,20,30,40,100])
# calculate the median using NumPy.
print(np.median(a))
# Then explain why the median is less affected by the 100 than the mean.
# yes it less affect
# 39. Variance

# Given:

# 1, 2, 3, 4, 5

# calculate:

# population variance
print(np.var)


# sample variance
print(np.var(a, ddof=1))
# using NumPy.

# 40. Standard deviation

# Calculate the standard deviation of:

# 1, 2, 3, 4, 5
a = np.array([1, 2, 3, 4, 5])
# Then verify it manually.
sum = 0 
count = 0 
for i in a :
    sum += i
    count += 1 
print(sum) 
manuallymean = sum /count
print(manuallymean)

variance  = 0 
for i in a :
    variance += (manuallymean-i)**2
variances  = variance / count
print(np.sqrt(variances))

print(np.std(a))

# 41. Percentiles

# Given:

# a = np.arange(1, 101)
a = np.arange(1, 101)
# find:

# 25th percentile
print(np.percentile(a,25))
# 50th percentile
print(np.percentile(a,50))
# 75th percentile
print(np.percentile(a,75))
# 90th percentile
print(np.percentile(a,90))
# 42. Correlation

# Create two arrays:

# study_hours
# exam_marks
# Calculate their correlation using NumPy.
study_hours = np.array([2,4,6,8])
exam_marks = np.array([40,60,80,100])
print(np.corrcoef(study_hours , exam_marks))

# Then explain what the correlation value means.
# it define as find the relation between to array they are related or not
# 🟠 Level 7 — Missing Data & Data Cleaning
# 43. Remove NaN

# Given:

# a = np.array([10, 20, np.nan, 40, np.nan, 60])
a = np.array([10, 20, np.nan, 40, np.nan, 60])
# remove all NaN values.
print(a[~(np.isnan(a))])

# 44. Count NaN values

# Find how many missing values exist in:

# a = np.array([1, np.nan, 3, np.nan, 5, np.nan])
a = np.array([1, np.nan, 3, np.nan, 5, np.nan])
count = 0
for i in a :
    if np.isnan(i) :
        count = count +  1
print(count)
print(np.isnan(a).sum())
# 45. Replace NaN with mean

# Given:

# a = np.array([10, 20, np.nan, 40, 50])
a = np.array([10, 20, np.nan, 40, 50])
# replace the NaN with the mean of the available values.
mean = np.nanmean(a)

a = np.where(np.isnan(a), mean, a)

print(a)

# 46. Remove invalid values

# Given:

# a = np.array([10, 20, -5, 30, -2, 40])
a = np.array([10, 20, -5, 30, -2, 40])
# remove all negative values using Boolean indexing.
a=a[ a > 0]
print(a)
# 🟠 Level 8 — Sorting & Searching
# 47. Sort an array

# Sort:

# a = np.array([50, 10, 30, 20, 40])
a = np.array([50, 10, 30, 20, 40])
# in ascending order.
print(np.sort(a))
# Then sort it in descending order.
print(np.sort(a)[::-1])
# 48. Find unique values

# Given:

# a = np.array([1, 2, 2, 3, 4, 4, 4, 5])
a = np.array([1, 2, 2, 3, 4, 4, 4, 5])
# find unique values.
print(np.unique(a))
# 49. Count occurrences

# Using NumPy, find how many times each value occurs.
print(np.bincount(a))
# 50. Find indexes

# Given:

# a = np.array([10, 50, 20, 80, 30])
a = np.array([10, 50, 20, 80, 30])
# find the index of the maximum and minimum values.
print(np.argmin(a))
print(np.argmax(a))
# 🔴 Level 9 — Linear Algebra

# These are very important for Machine Learning.

# 51. Matrix addition

# Given two 3 × 3 matrices, perform matrix addition.
a = np.arange(9).reshape(3,3)
print(a)
b = np.arange(9 , 18).reshape(3,3)
print(b)

c = a+ b
print(c)
# 52. Matrix multiplication

# Given:

# A = np.array([
#     [1, 2],
#     [3, 4]
# ])
A = np.array([
        [1, 2],
        [3, 4]
        ])
# B = np.array([
#     [5, 6],
#     [7, 8]
# ])
B = np.array([
        [5, 6],
        [7, 8]
        ])
# calculate:

# A × B

# using NumPy.
c = A * B
print(c)
print(np.multiply(A, B))
# 53. Dot product

# Calculate the dot product:

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a , b))
# 54. Transpose

# Find the transpose of a matrix using:

# np.transpose()
print(np.transpose(a))
# and .T.
print(a.T)
# 55. Determinant

# Calculate the determinant of:

# 1 2
# 3 4
a = np.array([[1,2] , [3,4]])
print(a)
print(np.linalg.det(a))
# using NumPy.

