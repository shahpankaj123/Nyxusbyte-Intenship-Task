def calculate_gcd(a, b):
    if b == 0:
        return a
    else:
        return calculate_gcd(b, a % b)
    
num1 =int(input("enter 1st number")) 
num2 = int(input("enter 2nd number"))

result = calculate_gcd(num1,num2)

print("The GCD of number",num1,"and number ",num2,"is :",result)
