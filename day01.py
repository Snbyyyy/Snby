'''time_=int(raw_input(">>"))
min_= time_// 60
times = time_ % 60
print(min_,times)

x,y,a,b,c = 1,1,0,0,0
part1 = ( 3+4*x) / 5
part2 = 10 * (y-5) *(a+b+c)/ x
part3 = 9 * ((4/x) + (9+x)/y)

res = part1 + part2 +part3
print(res)

'''
#1
'''
celsius = float (raw_input("Enter a degree in Celsius"))
celsius = float (celsius)
fahrenhit= float ((9.0/5.0)*celsius+32)
print(celsius,"Celsius is",fahrenhit,"Fahrenhit")
'''
#2
'''
radius,length = eval (raw_input("Enter the radius and length of a cylinder :"))
area = radius * radius * 3.14
volume = area * length
print("The area is",area)
print("The volume is",volume)
'''
#3
'''
a = float (raw_input("Enter a value for feet:"))
a = float (a)
b= float (a*0.305)
print(a,"feet is",b,"meters" )
'''
#4
'''
M = float (raw_input("Enter the amount of  water in kilograms:"))
initialTemperature = float (raw_input("Enter the initial Temperature :"))
finalTemperature = float (raw_input("Enter the final Temperature:"))
M = float (M)
initialTemperature = float (initialTemperature)
finalTemperature = float (finalTemperature)
Q = M * (finalTemperature - initialTemperature) * 4184.0
print("The energy needed is",Q)
'''
#5
'''
balance,interest = eval (raw_input('Enter balance and interest rate(e.g., 3 for 3%)'))
L = balance * (interest / 1200.0)
print("The interest is",L)
'''
#6
'''
v0,v1,t = eval (raw_input('Enter v0,v1,and t:'))
a=(v1-v0)/t
print('The average acceleration is',a)
'''
#7
'''
a = float(raw_input('Enter the mounthly saving amount:'))
a1 = a*1.00417
a2 = (a+a1)*1.00417
a3 = (a+a2)*1.00417
a4 = (a+a3)*1.00417
a5 = (a+a4)*1.00417
a6 = (a+a5)*1.00417
print('After the six month,the account valueis ',a6)
'''
#8
'''
a = float (raw_input('Enter a number between 0 an 1000:'))
b=a%10
c=a//10
d=c%10
e=c//10
f=b+d+e
print(f)
'''
#7
a = float (raw_input('Enter'))
n = 1
s = 0
while (n<=6):
 s=(a+s)*1.00417
 n=n+1
print(s)



