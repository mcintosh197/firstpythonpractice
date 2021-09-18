name = input("Enter your first name to begin >")

today = "02/03"
andreaDOB = "02/03"
brianDOB = "03/04"
clareDOB = "04/05"
daveDOB = "05/06"

def birthdayGreeting():
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday, to " + name)
    print("Happy Birthday to you")

if name == "Andrea" and today == andreaDOB:
    birthdayGreeting()

elif name == "Brian" and today == brianDOB:
    birthdayGreeting()

elif name == "Clare" and today == clareDOB:
    birthdayGreeting()

elif name == "Dave" and today == daveDOB:
    birthdayGreeting()

else:
    print("you are not authorised to use this system")

print("Logged in, taking you to the main menu…")
