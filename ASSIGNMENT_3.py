######################ASSIGNMENT 3########################
######LIST#####
#Q.1- Create a list with user defined inputs.
a=[]#creted a empty list
b=0
x=int(input("enter total no of element in list"))
for i in range(0,x):
    b=input("enter whatever u wanna add in list ")#taking input from user
    a.append(b) #here add that input in list
print(a)
#Q.2- Add the following list to above created list: [‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
x=[]#empty list
a=['google','apple','facebook','microsoft','tesla']
x.append(1)#add element in list x
x.append(2)#add element in list x
x.append(3)#add element in list x
x.append(4)#add element in list x
x.append(5)#add element in list x
x.append(a)#add list in list x
print(x)
#Q.3 - Count the number of time an object occurs in a list.
a=[]#creted a empty list
b=0
x=int(input("enter total no of element in list"))
for i in range(0,x):
    b=input("enter whatever u wanna add in list ")#taking input from user
    a.append(b) #here add that input in list
print(a)
m=input("enter what u wanna find in list")
cont=a.count(m)
if(cont>0):
    print("total no of element occur in list is ",cont)
else:
    print("ur search does not exist in this list")
    
#Q.4 - create a list with numbers and sort it in ascending order.
a=[]#creted a empty list
b=0
x=int(input("enter total no of element in list"))
for i in range(0,x):
    b=int(input("enter no to add in list "))#taking input from user
    a.append(b) #here add that input in list
    a.sort()
print(a)

#Q.5 - Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
a=[1,2,3,4,5,6]
b=[5,6,7,8,9,10]
c=[]#empty list
c=a+b# add both list in c
c.sort()#sort here
print(c)
#Q.6 - Count even and odd numbers in that list.
a=[]#creted a empty list
b=0
counteven=0
countodd=0
x=int(input("enter total no of element in list"))
for i in range(0,x):
    b=int(input("enter no to add in list "))#taking input from user
    a.append(b) #here add that input in list
    a.sort()
for i in range(0,len(a)):
    if a[i]%2==0:
        counteven=counteven+1
    else:
        countodd=countodd+1
print("total even element in the list is ",counteven)

print("total odd element in the list is ",countodd)


######TUPLES#######
#Q.1-Print a tuple in reverse order.
tup2=()
tup=('aa','bb')
tup=tup[::-1]
print(tup)
#Q.2-Find largest and smallest elements of a tuples.
tup=(1,2,3,4,5)
t=max(tup)
c=min(tup)
print(" max no in tuple is ",t)
print(" min no in tuple is ",c)

#######STRINGS#######
#Q.1- Convert a string to uppercase.
strr='hello world'
print(strr.upper())#change to upper case
#Q.2- Print true if the string contains all numeric characters.
strr='156465365'
print(bool(strr.isdigit()))
#Q.3- Replace the word "World" with your name in the string "Hello World". 
st='hello world'
strr1=st.replace('world','Viney Gautam')
print(strr1)


