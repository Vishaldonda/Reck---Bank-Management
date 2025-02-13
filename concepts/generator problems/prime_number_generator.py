# # Prime Number Generator : number divisible by number 1 and number itself 
# A prime number is a natural number greater than 1 that has exactly two distinct divisors: 1 and itself.

def prime_number_generator():
    n = 2
    while True: # Infinite loop
        is_prime = True
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                is_prime = False
                break   
        
        if is_prime:    
            yield n
        n+=1
        
        
gen = prime_number_generator()
n =  int(input("Enter a number to get first n prime numbers : ")) 

for _ in range(n):
    print(next(gen),end=" ")

