'''a = eval(raw_input('Enter'))
if a % 2 == 0:
    print('oushu')
else0:
    print('jishu')'''
#1
'''
import math
r = eval(raw_input('Enter the length from the center to a vertex :'))
s = 2 * r * math.sin(math.pi/5)
Area = (5*s*s)/(4*math.tan(math.pi/5))
print(Area)
'''
#2
'''
import math
x1,y1 = eval(raw_input("Enter point 1 (latitude and longitude) in degress"))
x2,y2 = eval(raw_input("Enter point 2 (latitude and longitude) in degress"))
part1 = math.sin(math.radians(x1))*math.sin(math.radians(x2))
part2 = math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y2-y1))
part3 = 6371.01 * math.acos(part1+part2)
print(part3)
'''
#3
'''
import math
s = eval(raw_input('Enter the side:'))
Area = 5 * pow(s,2)/ (4* math.tan(math.pi/5))
print(Area)
'''
#4
'''
import math
n = eval(raw_input("Enter the number of side:"))
s = eval(raw_input("Enter the side:"))
Area = n * pow(s,2)/(4*math.tan(math.pi/n))
print(Area)
'''
#5
'''
a = eval(raw_input('Enter an ASCII code'))
if 0<a<127:
    b = chr(a)
    print(b)
else:
    print("NO")
'''
#6
'''
Name = raw_input("Enter employee's name :")
week = eval(raw_input("Enter number of hours worked in a week:"))
hour = eval(raw_input("Enter hourly pay rate :"))
federal = eval(raw_input("Enter fedeal tax withholding rate:"))
state = eval(raw_input("Enter state taxwithholding rate:"))

print('Employee Name:',Name)
print("Hours Worked:",week)
print("Pay Rate",hour)
a = week * hour
print("Gross Pay",a)
print("Deductions:")
b = a * federal
c = a* state
d = b + c
f = a - d
print("   Federa Withholding (20.0%)",b)
print("   State Withholding(9.0%)",c)
print("   Total Deductions:",d)
print(' Net Pay',f)
'''
#7
'''
a = eval(raw_input('Enter an integer'))
b = a / 1000
c = a % 1000 / 100
d = a % 100 / 10
f = a % 10
print (str(f)+str(d)+str(c)+str(b)) 
'''
##1
'''
import math
a,b,c = eval(raw_input('Enter a,b,c:'))
D = pow(b,2)-4*a*c
if D>0:
    r1 =  (-b +math.sqrt(D))/2*a
    r2 =  (-b -math.sqrt(D))/2*a
    print('The roots are :',r1,r2)
elif D==0:
    r3 = -b/(2*a)
    print('The root is ',r3)
else:
    print('The equation has no real roots')
'''
##2
'''
import random
A = random.randint(0,100)
B = random.randint(0,100)
print(A,B)
C  = eval(raw_input("Enter the he"))
D = A+B
if D==C:
    print('True')
else:
    print('False')
'''
##3
'''
a = eval(raw_input("Enter today's day"))
b = eval(raw_input("Enter the number of days elapsed since today:"))
c = [0,1,2,3,4,5,6]
s = b % 7
print("{}day after is{}".format(b,c[a+s]))
'''
##4
'''
a,b,c = eval(raw_input("qing shu ru san ge shu "))
if a>b:
    a,b = b,a
if a>c:
    a,c = c,a
if b>c:
    b,c = c,b
print(a,b,c)
'''
##5
'''
a,b =  eval(raw_input("Enter weiht an price for package 1:"))
c,d = eval(raw_input("Enter weiht an price fir package 2:"))
E=a/b
F=c/d
if E>F:
    print('package 1 has better price')
else:
    print('package 2 has better price')
'''
##6
'''
a,b = eval(raw_input("Enter month,year"))
if a==2:
    if b%4==0:
        print(b,"nian",a,"yue you 29days")
    else:
        print(b,"nian",a,"yue you 28days")
elif a==1:
    print(b,"nian",a,"yue you 31days")
elif a==3:
    print(b,"nian",a,"yue you 31days")
elif a==5:
    print(b,"nian",a,"yue you 31days")
elif a==7:
    print(b,"nian",a,"yue you 31days")
elif a==8:
    print(b,"nian",a,"yue you 31days")
elif a==10:
    print(b,"nian",a,"yue you 31days")
elif a==12:
    print(b,"nian",a,"yue you 31days")

else:
    print(b,"nian",a,"yue you 30days")
'''
##7
'''
import random
a = eval(raw_input("Enter o or 1"))
b =random.randint(0,1)
if a==b:
    print("True")
else:
    print("False")
'''
##8
'''
import random

computer = random.randint(0, 2)
me = eval(raw_input("0 or 1 or 2 \n"))
if ((computer == 0 and me == 1) or
     (computer == 1 and me == 2) or
    (computer == 2 and me == 0)):  
    print("you won")
elif computer == me:  
    print("The computer is",me,"you are ",me,"too","It is a draw")
else:  
    print("you lose")
'''
##10
'''
import random
a = random.sample(["Ace","2",'3','4','5','6','7','8','9','10','Jack','Queen','king'],1)
b = random.sample(["hongtao","fangpian","meihua","heitao"],1)
print("you choice is",a,"of",b)
'''
##11
'''
a = eval(raw_input("Enter a shu"))
b = a//100
c = a%10
if b==c:
    print(a,"niubi")
else:
    print(a,"Sb")

'''
##12
a,b,c = eval(raw_input("sangeshu"))
e=a+b
f=a+c
g=b+c
if (e>c) and (f>b) and(g>a):
    d=a+b+c
    print(d,"niubi")
else:
    print("SB")





