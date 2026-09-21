#
#SEC290.13767.FA2022
#Christine Griffith
#10/09/22
#Week 6 Homework Assignment - Step 1
#

all_comments = []

prompt = "\nForum Comments\n==============\n0: Exit\n1: Display Comments\n2: Add Comment\n"
prompt += "\nPlease make a selection: "

active = True
while active:
    selection = input(prompt)

    if selection == "0":
        active = False
        print("Thank you for participating!")

    elif selection == "1":
        print("----------------------------------------------------------------------")
        for comment in all_comments:
            print(f"{comment['name']}\n{comment['comment']}")
            print("----------------------------------------------------------------------")

    elif selection == "2":
        name = input("What is your name? ")
        user_comment = input("Please add a one line comment: ")
        all_comments.append({'name': name, 'comment': user_comment})

    else:
        print("Please select 0, 1, or 2 only.")
