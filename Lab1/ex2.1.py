import sys
def do_stuff():
    number = int(sys.argv[1])
    if number < 2:
        print('No')
    else:
        for i in range(2, number):
            if number % i == 0:
                print('No')
                return
        print('Yes')
# Test the function
do_stuff()
#i) The code receives a user arguement from the terminal, checks if it is below 2, if not, it checks if it is a prime number and prints yes if it is
#ii) there was a quotation error to the right side of Yeson line 11