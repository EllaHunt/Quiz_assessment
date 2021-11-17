# functions


def quest_ask (question, answer):
    error = "please enter a number"
    global score
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response == answer:
                 print("correct")
                 score += 1
                 print('you got '+str(score)+' right!')
                 return response
            else:
                print("incorrect")
                return response
        except ValueError:
             print(error)


# main routine
show_instructions = ""
while show_instructions.lower() != "xxx":
    # ask the user if they have played before
    show_instructions = input ("have you played this Quiz before? ").lower()

    # if they say yes, output 'program continues'
    # if they say no, output 'display instructions'
    # if the answer is invalid, print an error.

    if show_instructions == "yes" or show_instructions == "y":
       show_instructions = "yes"
       print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
         show_instructions == "no"
         print("display instructions")

    else:
        print("please answer yes / no")
    score = 0
    q1 = quest_ask("what is 4 x 8 =?", 32)
    q2 = quest_ask("what is 10 - 6 =?", 4)
    q3 = quest_ask("what is 2 x 8 =?", 16)
    q4 = quest_ask("what is 12 x 2 =?", 24)
    q5 = quest_ask("what is 8 x 8 =?", 64)
    q6 = quest_ask("what is 10 - 7 =?", 3)
    q7 = quest_ask("what is 8 + 4 =?", 12)
    q8 = quest_ask("what is 12 - 7 =?", 5)
    q9 = quest_ask("what is 2 + 6 =?", 8)
    q10 = quest_ask("what is 6 x 10 =?", 60)
