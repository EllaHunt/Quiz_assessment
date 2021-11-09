# function goes here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response =="n":
            response = "no"
            return response

        else:
            print("please answer yes /no")


def instructions():
    print("**** how to play ****")
    print()
    print("the rules of the Quiz go here")
    print()
    return ""

# the main routine goes here...

played_before = yes_no("Have you played the Quiz before? ")

if played_before == "no":
    instructions()
else:
    print("program continues")
