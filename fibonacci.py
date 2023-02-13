#take the input from the user about the nu
n=int(input("Enter the number"))

def fibonacci():
    x=0
    print(x)
    y=1
    print(y)
    for i in range(n-2):
        temp=y
        y=x+y
        x=temp
        print(y)
       

fibonacci()
    