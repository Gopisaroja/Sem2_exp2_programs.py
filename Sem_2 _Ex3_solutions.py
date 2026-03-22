# Convert a list into tuple of lists
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
print(tuple(a))

# Menu-driven operations on a list
b = list(map(int, input("Enter list elements: ").split()))
while True:
    print("1.Maximum value\n2.Minimum value\n3.Slicing\n4.Count the number of occurances of any item\n5.Finding the first occurance of the item\n6.Exit")
    try:
        ch = int(input("Enter choice: "))
        if ch == 1:
            print(max(b))
        elif ch == 2:
            print(min(b))
        elif ch == 3:
            c, d = map(int, input("Enter start and end index: ").split())
            print(b[c:d])
        elif ch == 4:
            el = int(input("Enter the element to find the count: "))
            print(b.count(el))
        elif ch == 5:
            ele = int(input("Enter the element to find first occurance: "))
            print(b.index(ele))
        elif ch == 6:
            print("Exiting....")
            break
        else:
            print("Enter a valid choice!")
    except ValueError:
        print("Please enter a valid integer!")
    except IndexError:
        print("Please enter a valid index!")
    except Exception as err:
        print("Error:", err)

# Telephone directory using dictionary
dict = {}
for i in range(int(input("Enter no. of contacts: "))):
    name = input("Enter name: ")
    contact = input("Enter phone number: ")
    if len(contact) < 10:
        print("Enter valid phone number(10 digits)")
    elif len(contact) == 10:
        dict[name] = contact
print(dict)
print("What do you want? \n1.Mobile number\n2.Name of the person\n")
cho = int(input("Enter choice: "))
if cho == 1:
    name = input("Enter name: ")
    print(dict[name])
elif cho == 2:
    num = input("Enter number: ")
    for k, v in dict.items():
        if num == v:
            print(k)

# Squares of numbers from 1 to 9
print([j * j for j in range(1, 10)])

# Dictionary with squares of numbers 1 to 15
dict2 = {}
for i in range(1, 16):
    dict2[i] = i ** 2
print(dict2)

#  Hotel menu card using dictionary
hotel_menu = {"Parotta": 45, "Idli": 30, "Dosa": 40, "Poori": 35, "Biryani": 150}
print("---------Hotel menu---------\n")
for g, j in hotel_menu.items():
    print(g, ":₹", j)
food = input("Enter the food you want: ")
if food in hotel_menu:
    print("₹", hotel_menu[food])
else:
    print("Item not available")

# Sort list of tuples by last element
n = int(input("Enter number of tuples: "))
lst = []
print("Enter the elements:")
for i in range(n):
    elements = list(map(int, input(f"Tuple {i+1}: ").split()))
    tup = tuple(elements)
    lst.append(tup)
sorted_list = sorted(lst, key=lambda x: x[-1])
print("Sorted list:", sorted_list)

#  Transpose of matrix using list comprehension
mat = []
r, c = map(int, input().split())
for i in range(r):
    row = []
    for j in range(c):
        e = int(input())
        row.append(e)
    mat.append(row)
tr = [[mat[j][i] for j in range(r)] for i in range(c)]
for row in tr:
    print(*row)