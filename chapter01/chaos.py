# File: Chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("this program illustrates a chaotic function")
    x= eval(input ("Enter a number between 0 and 1: "))
    b= eval( input ("how many times do you want to loop"))
    for i in range (b):
        x=3.9 * x * (1-x)
        print(i + 1, ":", x)

main()

