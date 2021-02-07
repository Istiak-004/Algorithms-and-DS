# how to write a recursive function for any given problem for 3 steps
# step 1 : find the recursive flow
#step 2 : find the condition that will handle recursive flow 
#step 3 : solve the recursion for all condition

#find n factorial?
def Factorial(n):
	assert n>=0 and n==int(n) ,'this number cant be factorialed!' # assert {condition},{message}, if condition is not fullfilled then the message will be showned
	if n in [0,1]:
		return 1
	else:
		return n*Factorial(n-1)	
print(Factorial(4))		
