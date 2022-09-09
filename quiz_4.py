# # 1. Create a 2-D array and slice out the second number in the second column
sample = [[30, 45], [4, 3], [6, 7]]
print(sample)
sample[1:1].pop()


#2. Write a python program to sort array element in the ascending/descending order
num = int(input("Input size of array: "))
a = list(map(int, input("Enter element\n").split()))
def _ascending(list):
    a.sort()
    print(*a)
def _descending(list):
    a.sort(reverse = True)
    print(*a)

choice =input("Enter 'a' for ascending or 'd' for descending: ")
if choice == 'a':
    _ascending(a)
elif choice == 'd':
    _descending(a)

# 3. Write a python program to find the maximum and minimum value in a given 2-D array
import numpy as np

sample = np.array([5, 100], [4, 7], [8,10])
print("array is: ","\n, sample")
print("The minimum value from each row is: ","\n", np.min(sample, axis = 1), "\n")
print("The maximum value from each row is: ","\n", np.max(sample, axis = 1), "\n")

# #4.Write a python program to input 5 subject marks and calculate total marks, 
# percentage and grade based on following criteria
# # percentage less than 50 (Grade C)
# # percentage equal to 50 and less than 80 (Grade B)
# # percentage equal to 80 and more than 80 (Grade A)
totalmarks = 0
marks = list(map(int, input("Enter marks for the five subjects: \n").split()))
def tmarks(list):
    for mark in marks:
        totalmarks = totalmarks + mark
        print("Total marks are {totalmarks}")
    percentage = totalmarks/5
    if percentage < 50:
        print("Your grade is C")
    elif percentage == 50 and percentage < 80:
        print("Your grade is B")
    elif percentage >= 80:
        print("Your grade is A")

tmarks(marks)
