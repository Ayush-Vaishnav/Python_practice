'''
write generator fun that yields even number upto specified limit
'''

def even_generator(limit):
    for i in range(2, limit+1,2):
        yield i
    
for num in even_generator(10):
    print(num)

'''
A generator is like a function that can pause and resume its execution, instead of running all at once 
like a normal function. It yields values one at a time — on demand — using the yield keyword

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

#output
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen) again would raise StopIteration

'''