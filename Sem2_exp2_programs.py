#first repeated word in a string
d={}
a=list(input("Enter a string:").split())
flag=0
for i in a:
	if i in d:
		print(i)
		flag=1
		break
	else:
		d[i]=1
		flag=0
if flag==0:
	print("No repeated word!")
#count no. of characters
d={}
a=input("Enter a string:")
for i in a:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
print(d)
#count words
d={}
a=list(input("Enter a string:").split())
print(len(a))
for i in a:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
print(d)
#count upper and lower case letters
b=input("Enter a string:")
upper=0
lower=0
for i in b:
	if i.islower():
		lower+=1
	elif i.isupper():
		upper+=1
print(upper,lower)
#validate pan and name	
def isX(name):
    if name.replace(" ","").isalpha():
        return True
    else:
        return False
def isY(pan):
    if pan[0:5].isupper() and pan[0:5].isalpha() and pan[5:9].isdigit() and pan[9].isupper() and pan[9].isalpha():
        return True
    else:
        return False	
name = input("Enter name:")
pan = input("Enter pan number:")
print("Valid" if isX(name) and isY(pan) else "Invalid name or PAN number")
#ways of printing escape characters
print("Helloworld")
print("\\n This is a newline character \n purpose:\n Hello\nworld")
print("\\t This is horizontal tab\n purpose: Hello\tworld")
print("\\` This is  a single quote symbol\n purpose: \'Helloworld\'")
print('\\" This  a double quote symbol\n purpose:\"Helloworld\" ')
print("\\This is backslash symbol\n purpose:Hello\\world")
#adding ing or ly 
str=input("Enter a string:")
if len(str)>=3:
	if str.endswith("ing"):
		str+="ly"
		print(str)
	else:
		str+="ing"
		print(str)
#replace characters
s=input("Enter a string:")
s1=''.join(map(lambda ch:"j"if ch=='g' else ch,s))
print(s1)
