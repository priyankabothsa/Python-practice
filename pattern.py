#to print number pattern
"""
1
22
333
4444

r=int(input("enter rows:"))
for i in range(r+1):
    for j in range(i):
        print(i,end='')
    print('')"""
   
#to print pyramid pattern of numbers
"""
1
12
123
1234
12345
r=int(input("enter number of rows:"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end='')
    print('')"""
#to print inverted pyramid pattern of numbers
"""
11111
2222
333
44
5
r=int(input("enter no.of rows:"))
b=0
for i in range(r,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end='')
    print('')"""
#to print inverted pyramid pattern with same digit
"""
55555
5555
555
55
5
r=int(input("enter rows:"))
a=r
for i in range(r,0,-1):
    for j in range(0,i):
        print(a,end='')
    print('')"""
#to print inverted half pyramid with number
"""
012345
01234
0123
012
01
r=int(input("enter rows:"))
for i in range(r,0,-1):
    for j in range(0,i+1):
        print(j,end='')
    print("")"""
#to print alternate numbers printing using while loop
"""
1
33
555
7777
99999

r=int(input("enter rows:"))
i=1
while i<=r:
    j=1
    while j<=i:
        print((i*2-1),end='')
        j+=1
    i+=1
    print('')"""
#to print reverse number pattern
"""
55555
4444
333
22
1
r=int(input("enter no.of rows:"))
for i in range(r,0,-1):
    a=i
    for j in range(0,i):
        print(a,end='')
    print('')"""
#to print reverse pyramid of numbers
"""
1
21
321
4321
54321
r=int(input("enter no.of rows:"))
for i in range(1,r):
    for j in range(i,0,-1):
        print(j,end='')
    print('')
"""
#to print reverse number pattern
"""
54321
4321
321
21
1

r=int(input("enter no.of rows:"))
for i in range(0,r+1):
    for j in range(r-i,0,-1):
        print(j,end='')
    print('')"""
#to print reverse number from 10 to 1
"""
1
32
654
10987
start=1
stop=2
current_num=stop
for row in range(2,6):
    for col in range(start,stop):
        current_num-=1
        print(current_num,end='')
    print('')
    start=stop
    stop+=row
    current_num=stop"""
#to print number triangle program
"""
    1
   12
  123
 1234
12345

r=int(input("enter no.of rows:"))
for i in range(1,r):
    num=1
    for j in range(r,0,-1):
        if j>i:
            print(" ",end='')
        else:
            print(num,end='')
            num+=1
    print('')
    """
#to print pascal triangle using numbers
"""
      1
     1 1
    1 2 1
   1 3 3 1 
  1 4 6 4 1
 1 5 10 10 5 1
1 6 15 20 15 6 1

n=int(input("enter no.of rows:"))
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print(' ',end=' ')
    c=1
    for j in range(1,i+1):
        print(' ',c,sep=' ',end=' ')
        c=c*(i-j)//j
    print(' ')"""
#to print square pattern with numbers
"""
12345
22345
33345
44445
55555

r=int(input("enter no.of rows:"))
for i in range(1,r+1):
    for j in range(1,r+1):
        if j<=i:
            print(i,end='')
        else:
            print(j,end='')
    print()
"""
#to print multiplication table pattern
"""
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36

r=int(input("enter no.of rows:"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(i*j,end=' ')
    print()
"""
#to print pyramid pattern of stars in python
"""
*
**
***
****
*****

r=int(input("enter no.of rows:"))
for i in range(0,r):
    for j in range(0,i+1):
        print("*",end='')
    print()
"""
#to print right triangle pyramid of stars
"""
*
**
***
****
*****

r=int(input("enter no.of rows:"))
for i in range(0,r):
    for j in range(0,i+1):
            print("*",end='')
    print('')
"""
#to print right triangle pyramid of stars
"""
        *
       **
      ***
     ****
    *****
 
r=int(input("enter no.of rows:"))
k=2*r-2
for i in range(0,r):
    for j in range(0,k):
        print(end=' ')
    k=k-2
    for j in range(0,i+1):
        print("* ",end='')
    print('')
   """
#to print downward half pyramid pattern of stars
"""
*****
****
***
**
*

r=int(input("enter no.of rows:"))
for i in range(r+1,0,-1):
    for j in range(0,i-1):
        print("*",end='')
    print('')
"""
#to print downward full pyramid pattern of star
"""
 *******
  *****
   ****
    ***
     **
      *

r=int(input("enter no.of rows:"))
k=2*r-2
for i in range(r,-1,-1):
    for j in range(k,0,-1):
        print(end=' ')
    k=k+1
    for j in range(0,i+1):
        print("*",end=' ')
    print(' ')
"""
#to print right down mirror star pattern
"""
*****
 ****
  ***
   **
    *
r=int(input("enter no.of rows:"))
i=r
while(i>=1):
    j=r
    while(j>i):
        print(' ',end=' ')
        j-=1
    k=1
    while(k<=i):
        print(" *",end='')
        k+=1
    print()
    i-=1
"""
#to print equilateral triangle of stars
""" 
            *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  *  

r=int(input("enter no.of rows:"))
m=(2*r)-2
for i in range(0,r):
    for j in range(0,m):
        print(end=' ')
    m=m-1
    for j in range(0,i+1):
        print("* ",end=' ')
    print(' ')
"""
#to print two pyramid of stars
"""
*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*  

r=int(input("enter no.of rows:"))
for i in range(0,r):
    for j in range(0,i+1):
        print("*",end=' ')
    print(' ')
for i in range(r+1,0,-1):
    for j in range(0,i-1):
        print("*",end=' ')
    print(' ')
"""
#to print right star or right pascal's triangle
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

r=int(input("enter no.of rows:"))
for i in range(0,r):
    for j in range(0,i+1):
        print("*",end=' ')
    print(' ')
for i in range(r,0,-1):
    for j in range(0,i-1):
        print("*",end=' ')
    print(' ')
"""
#to print left pascal triangle
"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
r=int(input("enter no.of rows:"))
i=1
while i<=r:
    j=i
    while j<r:
        print(' ',end=' ')
        j+=1
    k=1
    while k<=i:
        print("*",end=' ')
        k+=1
    print()
    i+=1
i=r
while i>=1:
    j=i
    while j<=r:
        print(' ',end=' ')
        j+=1
    k=1
    while k<i:
        print('*',end=' ')
        k+=1
    print(' ')
    i-=1
"""
#to print sandglass pattern of star
"""
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

r=int(input("enter no.of rows:"))
i=0
while i<=r-1:
    j=0
    while j<i:
        print('',end=' ')
        j+=1
    k=i
    while k<=r-1:
        print("*",end=' ')
        k+=1
    print()
    i+=1
i=r-1
while i>=0:
    j=0
    while j<i:
        print('',end=' ')
        j+=1
    k=i
    while k<=r-1:
        print("*",end=' ')
        k+=1
    print('')
    i-=1
"""
#to print pant style pattern of stars
"""
****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*

r=int(input("enter no.of rows:"))
print("*" * r,end="\n")
i=(r // 2)-1
j=2
while i != 0:
    while j<=(r-2):
        print("*" * i,end="")
        print("_" * j,end="")
        print("*" * i,end="\n")
        i=i-1
        j=j+2
"""
#to print diamond shaped pattern of stars
"""
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 

r=int(input("enter no.of rows:"))
k=2*r-2
for i in range(0,r):
    for j in range(0,k):
        print(end=' ')
    k=k-1
    for j in range(0,i+1):
        print("* ",end="")
    print("")
k=r-2
for i in range(r,-1,-1):
    for j in range(k,0,-1):
        print(end=' ')
    k=k+1
    for j in range(0,i+1):
        print("* ",end='')
    print('')
"""
#to print diamond pattern of star
"""
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *

#upper part
r=int(input("enter no.of rows:"))
for i in range(1, r+1):
    for j in range(1,r-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part
for i in range(r-1,0, -1):
    for j in range(1,r-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
"""
#to print alphabetical order
"""
A
BC
DEF
GHIJ
KLMNO
PQRSTU
VWXYZ[/

ascii_number=65
r=int(input("enter no.of characters:"))
for i in range(0,r):
    for j in range(0,i+1):
        c=chr(ascii_number)
        print(c,end=' ')
        ascii_number+=1
    print(" ")
"""
#to print display letter of the word
"""
p
pr
pri
priy
priya
priyan
priyank
priyanka

w=input("enter your word:")
x=" "
for i in w:
    x+=i
    print(x)
"""
#to print equilateraltriangle pattern of alphabets
"""
            A  
           B C  
          D E F  
         G H I J  
        K L M N O  
       P Q R S T U  
      V W X Y Z [ \  
print("print Equilateral triangle pyramid with characters")
s=int(input("enter your size:"))
ascii=65
m=(2*s)-2
for i in range(0,s):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        c=chr(ascii)
        print(c,end=' ')
        ascii+=1
    print(" ")
"""
#to print pattern of same character
"""
A
AA
AAA
AAAA
AAAAA

c=input("enter your character")
char=ord(c)
for i in range(0,5):
    for j in range(0,i+1):
        user=chr(char)
        print(user,end=' ')
    print()
"""
#to print double the number pattern
"""
   1 
   2    1 
   4    2    1 
   8    4    2    1 
  16    8    4    2    1 
  32   16    8    4    2    1 
  64   32   16    8    4    2    1 
 128   64   32   16    8    4    2    1 

r=int(input("enter no.of rows:"))
for i in range(1,r):
    for j in range(-1+i,-1,-1):
        print(format(2**j,"4d"),end=' ')
    print(" ")
"""
#to print pyramid of numbers less than 10
"""
1
234
56789
c=int(input("enter the current num:"))
s=int(input("enter when to stop:"))
r=int(input("enter no.of rows:"))
for i in range(r):
    for j in range(1,s):
        print(c,end=' ')
        c+=1
    print(" ")
    s+=2
"""

"""n=int(input("Enter the number of rows:"))
for i in range(n):
	for j in range(n):
		if j==0 or i==(n-1) or i==j:
			print("*",end="")
		else:
			print(end=" ")
	print()
"""
"""
n=int(input("Enter the number of rows:"))
for i in range(n):
	for j in range(n):
		if j==0 or i==(n-1) or i==j:
			print("*",end="")
		else:
			print(end=" ")
	print()
"""
#floyd's triangle
"""
1
23
456
78910

n=int(input("enter no.of rows:"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()
"""
#to print hollow equilateral triangle
"""
    *   
   * *   
  *   *  
 *     * 
*********
n=int(input("enter no.of rows:"))
for i range(1,n+1):
    for j in range(1,2*n):
        if i==n or i+j==n+1 or j-i==n-1:
            
"""
"""
n=int(input("enter no.of rows:"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
"""
