a, b = 1, 1 
Fi = 0 
while a <= 4000000: 
    if a % 2 == 0:
        Fi += a 
    a, b = b, a+b #the real formula for Fibonacci sequence 

print(Fi)


#def fibonacci(n): #recursive, n - sequence number of element which we want to see
   #if n in (1, 2):
        #return 1 #because second element of Fibonaacci sequence =1
    #return fibonacci(n - 1) + fibonacci(n - 2)


#print(fibonacci(3)) #third element of Fibonacci sequence (1 1 2 3), third = 2

#Допустим, n = 4. Тогда произойдет рекурсивный вызов fibonacci(3) и fibonacci(2).
#Второй вернет единицу, а первый приведет к еще двум вызовам функции:
#fibonacci(2) и fibonacci(1). Оба вызова вернут единицу, в сумме будет два.
#Таким образом, вызов fibonacci(3) возвращает число 2,
#которое суммируется с числом 1 от вызова fibonacci(2).
#Результат 3 возвращается в основную ветку программы.
#Четвертый элемент ряда Фибоначчи равен трем: 1 1 2 3. - Fibonacci sequence!





#fib1 = fib2 = 1

#n = int(input("Номер элемента ряда Фибоначчи: ")) - 2#because fib 3 = fib1 +fib 2

#while n > 0:
    #fib1, fib2 = fib2, fib1 + fib2
    #n -= 1 #counter of iterations

#print(fib2)
