# Made changes to the code to make it more comprehensive

# Asking the user for inputs 
print('Please enter the dividend :')
dividend = int(input(''))
print('Please enter the divisor :')
divisor = int(input(''))

while True:
    # Checking divisibility
    if dividend % divisor == 0:
        print('Success!',divisor,'divides the dividend')
        break
    print(divisor,'does not divide the dividend')
    break
