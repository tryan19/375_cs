#average_calculator.py
#test scores to test average
#by: Tom Ryan


def main():
    score=input("whats the score?")
    total=0
    scores=0
    while score!="":
        print(score)
        total = total + eval(score)
        score = input("whats the next score?")
        scores = scores +1
    averages = total / scores
    print("your average is" , averages)


main()
