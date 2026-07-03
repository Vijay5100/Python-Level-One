'''
Brute Force: 
We will try all the possible combinations of 
texts+symbols+numbers 
8 digits 
text - 26 + 26 = 52 
symbols - 20 
numbers - 0 to 9 
total = 82

_ _ _ _ _ _ _ _ _ 
82 X 8 

there are 3.7 quadrillion possibilities 
it takes 1.17 billion years to test all the possibilities
Quantum computers take just 42.8 days to try all the possibilities


111 -> 2 ** n 
'''
number_of_digits = int(input("Characters Length: "))
password = input("Password: ")
possibilities = 2 ** number_of_digits
dictonary = [] 
for i in range(possibilities):
    binary = bin(i)[2:]
    binary = binary.replace("1","b")
    binary = binary.replace("0","a")
    dictonary.append(binary)
for i in range(2,possibilities):
    binary = bin(i)[2:]
    binary = binary.replace("1","a")
    binary = binary.replace("0","b")
    dictonary.append(binary)

for guess in dictonary:
    if guess == password:
        print(guess)
        break 
    

"""
_ _ _ _ 
a 
a a a a 
a a a b 
a a a c 

_ _ 
  a 0 0 
  b 0 b
b b 
b a 

"""
