# Q1. Write a program that takes salary as input. Using conditional statements, 
# calculate the final tax rate based on these rules: 
# • If salary < 30,000 → 5% 
# • If salary is 30,000–70,000 → 15% 
# • If salary > 70,000 → 25%


salary = int(input("Enter your salary:"))

if(salary <  30000):
    print(salary * 0.5)
elif(salary < 30000 and salary < 70000):
    print(salary * 0.15)
elif(salary > 70000):
    print(salary * 0.25)
        
