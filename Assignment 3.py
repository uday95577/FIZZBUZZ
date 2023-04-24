z = int(input("Please enter any number: "))
if(z % 3 == 0 and z % 5 == 0):
    print('FIZZBUZZ')
elif(z % 3 == 0):
    print('FIZZ')
elif(z % 5 == 0):
    print('BUZZ')
elif(z % 3 != 0 and z % 5 != 0):
    print(z)