# !/usr/bin/env python3

import os


def git_add():
    first_prompt = input("Do you wish to add all files to git? y/n ")
    if first_prompt.lower() == "y":
        os.system("git add .")
    elif first_prompt.lower() == "n":
        filename = input("enter file name to add: ")
        os.system("git add " + filename)


def git_commit():
    os.system("git commit -m " + input(" "))


def git_status():
    print("Getting git status...")
    os.system("git status")

def git_push():
    third_prompt = input("Do you wish to push the the committed changes? y/n ")
    y = "yes"
    n = "no"
    if third_prompt == y.lower():
        os.system("git push")
    elif third_prompt == n.lower():
        print("Arborted")

        #you have not pushed the commit publicly yet, 
        #your commit changes will be in your working directory, 
        # whereas the LAST commit will be removed from your current branch.
        os.system("git reset HEAD~1 --soft ") 


if __name__ == '__main__':
    git_add()
    git_commit()
    git_status()
    git_push()