# Simulated authorization code

ownerID = 9001

def ShowData():
    print("This is the account balance")

def Redirect():
    print("Redirecting to homepage")

def GetUserID():
    return 1111

if GetUserID() != ownerID:
    print("You are not allowed to view this data")
    Redirect()
else:
    ShowData()
