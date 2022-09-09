

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
