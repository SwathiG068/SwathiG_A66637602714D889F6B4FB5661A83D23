def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n*fact_rec(n-1)

#Main Program
num = int(input("Enter the value : "))
result = fact_rec(num)
print("The Factorial of {} is {}".format(num, result))
