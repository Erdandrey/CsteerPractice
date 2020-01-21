PassDict = dict()
UidDict = dict()
GroupDict = dict()
with open('/etc/passwd', 'r') as FilePass:
    for line in FilePass:
        Wrapper = line[line.rfind(':'):len(line) - 1]
        UID = line.split(':')
        UidDict.update({UID[0]: UID[2]})
        if PassDict.get(Wrapper) is None:
            PassDict.update({Wrapper: 1})
        else:
            PassDict[Wrapper] = PassDict[Wrapper] + 1
with open('/etc/group', 'r') as FileGroups:
    for line in FileGroups:
        Group = line[:line.find(':')]
        User = line[line.rfind(':')+1:len(line) - 1]
        if User != '':
            UserList = User.split(',')
            UserCodes = ' '
            for value in UidDict.keys():
                if UserList.count(value) != 0:
                    UserCodes = UserCodes + UidDict[value]+' '
                    GroupDict.update({Group: UserCodes})
with open('./output.txt', 'w') as Final:
    Final.write(str(PassDict))
    Final.write('\n')
    Final.write((str(GroupDict)))


