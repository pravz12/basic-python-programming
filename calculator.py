# Return sum of num1 and num2
def add(num1,num2):
    return num1+num2
#return diff of num1 and num2
def diff(num1,num2):
     return num1-num2
#return multiplication of num1 and num2
def product(num1,num2):
    return num1*num2
#return division of num1 and num2
def division(num1,num2):
    return num1/num2
	
def main():
    operation = raw_input("what do you want to do (+,-,*,/):")
    if(operation != '+' and operation != '-' and operation != '*' and operation != '/'):
      # invalid operation 
      print("you must enter a valid operation")
    else:
        var1= int(input("enter num1:"))	
	var2= int(input("enter num2:"))  
	if(operation =='+'):
	   print(add (var1,var2))
	elif(operation =='-'):
	   print(diff(var1,var2))
	elif(operation =='*'):
	   print(product(var1,var2))
	else:
	   print(division(var1,var2))
main()
	    
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
   
      
