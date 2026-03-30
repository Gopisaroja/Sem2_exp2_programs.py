#volume of cuboid using positional arguments
def volume(a,b,c):
	return a*b*c
a,b,c=map(int,input("Enter length,breadth,height of cuboid:").split())
print(volume(a,b,c))
#sum to the series
import math
def sumseries(a):
	tot=0
	for i in range(1,a+1):
		tot+=(i*i)/math.factorial(i)
	return tot
a=int(input("Enter a number to find the sum of series:"))
print(sumseries(a))
#to check whether numbers are equal or not
def equalornot(a,b):
	if a==b:
		return "They are equal"
	else:
		return "They are not equal"
a,b=map(int,input("Enter two numbers:").split())
print(equalornot(a,b))
#to convert into upper case
def upper(s):
	return s.upper()
a=input()
print(upper(a))
#import modules
def new(num):
    total = sum(num)
    avg= total / len(num)
    mini = min(num)
    maxi = max(num)
    return total, avg, mini, maxi
    
import newfile

l = [1, 5, 6, 7]
total, avg, min_val, max_val = newfile.new(l)
print(f"Sum: {total}, Average: {avg}, Min: {min_val}, Max: {max_val}")


#import statistics
import statistics
n=list(map(int,input().split()))
print("Mean:",statistics.mean(n))
print("Standard deviation:",statistics.stdev(n))
print("Mode:",statistics.multimode(n))
print("Variance:",statistics.variance(n))
print("Median:",statistics.median(n))
#filter persons using age
ch=int(input("Enter number of dictionaries:"))
a=int(input("Enter age:"))
def validity(ch,a):
	lst=[]
	dct={}
	for i in range(ch):
			name=input("Enter name:")
			age=int(input("Enter age:"))
			dct[name]=age
	lst.append(dct)
	for d in lst:
			for name,age in dct.items():
					if age>a:
						print(name,age)
validity(ch,a)
#area of rectangle
xh=int(input("Enter how many rectangles:"))
def area(xh):
	tup1=()
	for j in range(xh):
		a,b=map(int,input().split())
		tup=(a,b)
		tup1+=(tup,)
	for a,b in tup1:
		print(a*b)
area(xh)
#a number can be expressed as sum of primes or not?
def prime(n):
	if n<=1:
		return False
	else:
		for i in range(2,int(n/2)+1):
				if n%i==0:
					return False
					break
	return True
n=int(input())
lst=[i for i in range(2,n) if prime(i)]
flag=0
for j in lst:
		for g in lst:
			if g+j==n:
				flag=1
				print(j,g)
if flag==0:
			print("Not found")			
#gcd
def gcd(a,b):
	while b!=0:
		a,b=b,a%b
	return a
a,b=map(int,input().split())
print(gcd(a,b))	
#tuple that contains only positive numbers
a=list(map(int,input().split()))
c=[]
for i in a:
	if i>0:
		c.append(i)
	else:
		pass
print(tuple(c))
#to find a largest string in sentence and remove duplicates
s=list(input().split())
a=[]
for i in s:
	l=len(i)
	a.append(l)
b=list(set(s[a.index(max(a))]))
print(''.join(b))