import getrepolist

def createPR():
    print("created PR")
    list = getrepolist.getgithubrepolist()
    print(list)
    print("chnage in PR ")

createPR()