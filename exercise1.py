# fibonacci sequence calculation

def main():
      sum = 0.0
      n = eval(input("What is your nth number in the sequence? "))
      if n==1 or n==2:
            x=1
      else:
            for i in range(2,n):
                  x = (x(n-1) + x(n-2))
      print("\nYour Fibonacchi number for n is: ", x)

main()

               
