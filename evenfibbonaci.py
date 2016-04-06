def fib(n):
    '''
    Generate next term in Fibonacci sequence.
    Append next term to list.
    Return list of Fibonacci terms.
    '''
    a,b = 1,1
    while b <= n:
        a,b = b,a+b
        fib_sequence.append(a)
    return fib_sequence

def find_even_terms(n):
    '''
    Loop through elements in list to find even terms.
    Keep running total of even terms.
    Return sum of even terms.
    '''
    sum_even_terms = 0
    for n in fib_sequence:
        if n % 2 == 0:
            print n
            sum_even_terms = sum_even_terms + n
    return sum_even_terms

fib_sequence = []
x = fib(4000000)
print "Sum of even Fibonacci terms: " + str(find_even_terms(x))
