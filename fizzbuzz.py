# fizzbuzz printing number 1-100

for num in range (1,101):


#number is multiple of 3 print "fizz"
#number is multiple of 5 print "buzz"
#number is multiple of both 5 & 3 print "fizzbuzz"

    if num % 3 == 0 and num % 5 == 0:
        print ("FizzBuzz")
        continue
    elif num % 3 == 0:
        print ("Fizz")
        continue
    elif num % 5 == 0:
        print("Buzz")
        continue

    print(num)

