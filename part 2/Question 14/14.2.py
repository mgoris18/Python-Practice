ownerID = 2222

def ShowData():
    print("This is the order history")

def Redirect():
    print("Redirecting to homepage")

def GetUserID():
    return 3333

def AccessObject():
    if GetUserID() != ownerID:
        print("You are not allowed to view this data")
        Redirect()

    else:
        ShowData()

AccessObject()
