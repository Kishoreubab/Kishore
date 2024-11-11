data = [110, 301, 23, 37, 100, 999, 37, 3513]
result = filter (lambda x:x > 4, data)
print (list(result))



my_list = [1, "hello", 3, "world", 5]
print("The original list : " + str(my_list))
result1 = [element for element in my_list if isinstance(element, str)]
print("The string instances : " + str(result1))
result2 = [element for element in my_list if isinstance(element, int)]
print("The integer instances : " + str(result2))




def fibonacci(count):
    a = 0
    b = 1
    fib_list = [a,b]
    for _ in range(count):
        fib_list.append(a)
        a, b = b, a + b         
    return fib_list
print(fibonacci(50))




import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return "It's a Valid E-mail id"
    else:
        return "It's a Invalid E-mail id"

def validate_bangladesh_mobile_number(number):
    pattern = r'^\+8801[3-9]\d{8}$'
    if re.match(pattern, number):
        return "It's a Valid Phone Number" 
    else:
        return "It's a Invalid Phone Number"
    
def validate_usa_telephone_number(number):
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    if re.match(pattern, number):
        return "It's a Valid Phone Number" 
    else:
        return "It's a Invalid Phone Number"

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{16}$'
    if re.match(pattern, password):
        return "It's a Valid Password" 
    else:
        return "It's a Invalid Password" 

def main():
    email = input("Enter your email: ")
    print(validate_email(email))
    
    number = input("Enter your Bangladesh mobile number: ")
    print(validate_bangladesh_mobile_number(number))  
    
    usa_number = input("Enter your USA telephone number: ")
    print(validate_usa_telephone_number(usa_number))  
    
    password = input("Enter your password: ")
    print(validate_password(password))

if __name__ == "__main__":
    main()

#Note Examples Valid output are 1-test.email@example.com, 2-+8801712345678, 3-(123) 456-7890, 4-Test1234@Passwor
#Note Examples Invalid output are 1-valid-email.com , 2-+8801012345678, 3-123-456-789, 4-short1@
