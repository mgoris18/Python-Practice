ownerID = 5555

def ShowData():
    print("This is the billing information")

def Redirect():
    print("Redirecting to homepage")

def GetUserID():
    return 1234

def AccessObject():
    if GetUserID() != ownerID:
        print("You are not allowed to view this data")
        Redirect()
    else:
        ShowData()

AccessObject()
