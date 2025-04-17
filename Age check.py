#ask user for age and save it in the 'userAge' variable
userAge = int(input("How old are you?: "))

#define a function that checks is user can vote
def userVotingStatus(n):
    if n>= 18:
        print("You can vote!")
    else:
        print("You're too young to vote.")
#call function
userVotingStatus(userAge)
