def factorize_number(x): 
 divisor=2 
 while x>1: 
  if x % divisor==0:
      x//=divisor 
  else:
      divisor+=1 
      
 print(divisor)
factorize_number(600851475143)
