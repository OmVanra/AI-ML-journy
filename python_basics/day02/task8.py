# Q8. Letʼs create a Simple Calculator that performs arithmetic operations. Create 
# a function calculator(a, b, operation) that performs addition, subtraction, 
# multiplication, or division based on the operation parameter. 
# [ 
# operation 
# parameter can have values , , & .

def calculator(a,b, operation):
    if (b > 0):
        if(operation == '+'):
            return a + b
        elif(operation == '-'):
            return a - b
        elif(operation == '*'):
            return a * b
        else:
            return a / b
    else:
        print("please enter b greater than 0")    
        
print(calculator(2,3,'/'))        