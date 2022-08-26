from time import *
import random as r

def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s, time_e, user_input):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(user_input)/time_R
    return round(speed)


if __name__ == '__main__':
    while True:
        ck = input("Ready to test: yes/no:")

        if ck == "yes":
            test = ["my name is shubham yadav.",
                    "welcome to my word.",
                    "what you want."]
            test1 = r.choice(test)
            print("~>Typing speed<~")
            print(test1)
            print()
            print()

            time_1 = time()
            test_input = input("Enter :")
            time_2 = time()

            print("speed : ", speed_time(time_1, time_2, test_input),"w/sec")
            print("Error: ", mistake(test1, test_input))
        elif ck == "no":
            print("thank you")
            break
        else:
            print("Wrong Input")
