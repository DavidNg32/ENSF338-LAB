import timeit

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    start_for = timeit.default_timer()
    for i in range(10000):
        factorial(100)
    stop_for = timeit.default_timer()
    print('Time taken using for loop: ', stop_for - start_for)
    
    start_list_comprehension = timeit.default_timer()
    for _ in range(1000):
        list(map(factorial, range(1, 101)))
    stop_list_comprehension = timeit.default_timer()
    
    print('Time taken using list comprehension: ', stop_list_comprehension - start_list_comprehension)