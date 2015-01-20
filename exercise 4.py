# syracuse sequence

def main():
      Number = eval(input("Please enter a number: "))
      print("")

      count = 0
      print(Number)
      while Number !=1:
            if(Number % 2==0):
                  use = number//2
                  print(use)
                  Number = use
                  count = count + 1

            else:
                  use = Number*3+1
                  print (use)
                  Number = use
                  count = count + 1

      print("")
      print(str(count) + "computations performed")
      print("")

main ()
