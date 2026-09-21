#
#SEC290.13767.FA2022
#Christine Griffith
#10/09/22
#Week 6 Homework Assignment - Step 3
#

import os

filename = 'step3_data.txt'
all_comments = []

if os.path.exists(filename):
    with open(filename) as text_file:
        text_file.readline()  # skip the header row
        for line in text_file:
            line = line.strip()
            if not line:
                continue
            name, comment = line.split('\t')
            all_comments.append({'name': name, 'comment': comment})
else:
    with open(filename, 'w') as text_file:
        text_file.write("Name\tComment\n")

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
        new_comment = {'name': name, 'comment': user_comment}
        all_comments.append(new_comment)

        with open(filename, 'a') as text_file:
            text_file.write(f"{name}\t{user_comment}\n")

    else:
        print("Please select 0, 1, or 2 only.")
