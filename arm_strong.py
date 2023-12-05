num = int(input("Enter a number: "))      # take input from the user
sum = 0                                   # initialize sum
temp = num                                # find the sum of the cube of each digit
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:                             
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")