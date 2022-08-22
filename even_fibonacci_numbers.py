a, b = 1, 1 
Fi = 0 
while a <= 4000000: 
    if a % 2 == 0:
        Fi += a 
    a, b = b, a+b #the real formula for Fibonacci sequence 

print(Fi) #sum of the even-valued terms

#def fibonacci(n):
   #if n in (1, 2):
        #return 1
    #return fibonacci(n - 1) + fibonacci(n - 2)


#print(fibonacci(3)) 
