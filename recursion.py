# how to write a recursive function for any given problem for 3 steps
# step 1 : find the recursive flow
#step 2 : find the condition that will handle recursive flow 
#step 3 : solve the recursion for all conditions/find the bug inside the code/unintensional case

#find n factorial?
def Factorial(n):
	assert n>=0 and n==int(n) ,'this number cant be factorialed!' # assert {condition},{message}, if condition is not fullfilled then the message will be showned
	if n in [0,1]:
		return 1
	else:
		return n*Factorial(n-1)	
print(Factorial(4))		

# Fibonnacchi number
def Fibonacchi(n):
	assert n>=0 and int(n)==n ,'fibonacchi seq cant not be neg or float'
	if n in [0,1]:
		return n
	else:
		return Fibonacchi(n-1)+Fibonacchi(n-2)
print(Fibonacchi(9))

# those two problem using loop
#factorial
def factorial(n):
	if n ==0:
		return 1
	fact_num = 1
	i=1
	while i<=n:
		fact_num = fact_num*i
		i+=1
	return fact_num
print(factorial(4))

#fibonacchi
def fibonacchi(n):
	a = 0
	b = 1
	if n==0:
		return a
	elif n==1:
		return b
	elif n<0:
		return 'neg number isnt count'
	else:
		for i in range(1,n):
			c = a+b
			a=b
			b=c
		return b,i
print(fibonacchi(9))					
