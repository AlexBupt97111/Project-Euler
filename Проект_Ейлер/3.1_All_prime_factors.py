def factorize_number(x): 
 divisor=2 
 while x>1: #while x more than 1
  if x % divisor==0:
      x//=divisor
      print(divisor) 
  else:
      divisor+=1 #if x&div!=0  - add to divisor 1
      
factorize_number(600851475143)
