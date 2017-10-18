#speen_convert.py
#meters per second to miles per hour
#by: Tom Ryan


def main():
    meterspersecond = eval(input("What is the meters per second  "))
    #60 sec/min * 60 min/hour = 3600 sec/hour
    milesperhour= (3600/1609) * meterspersecond
    if meterspersecond<= 0:
        print("invalid input")
    else: print("the miles per hour is", milesperhour,)



main()



