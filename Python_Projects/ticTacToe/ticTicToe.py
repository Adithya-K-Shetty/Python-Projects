board={'topl':{'value':' ','pos':1},'topm':{'value':' ','pos':2},'topr': {'value':' ','pos':3},'midl':{'value':' ','pos':4},'midm':{'value':' ','pos':5},'midr':{'value':' ','pos':6},'lowl':{'value':' ','pos':7},'lowm':{'value':' ','pos':8},'lowr':{'value':' ','pos':9}}

winningPosition = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]] 
def ticTacToe(userList):
        print(userList['topl']['value'] + "|" + userList['topm']['value'] + "|" + userList['topr']['value'])
        print('-+-+-')
        print(userList['midl']['value'] + "|" + userList['midm']['value'] + "|" + userList['midr']['value'])
        print('-+-+-')
        print(userList['lowl']['value'] + "|" + userList['lowm']['value'] + "|" + userList['lowr']['value'])
        return ''
ticTacToe(board)

userMove = True

list1 = []
list2 = []   
flag = 0
movCounter = 0
for move in range(20):
    if userMove == True:
        x = input("Player X, enter the position : ").lower()
        if board[x]['value'] == ' ':
            board[x]['value'] = 'x' 
            movCounter+=1
        else:
            print("position already occupied")
            continue
        print(ticTacToe(board))
        list1.append(board[x]['pos']) 
        for winPos in winningPosition:
            counter = 0
            for individualPos in winPos:
                if individualPos in list1:
                    counter+=1
                if counter == 3:
                    flag = 1
                    break
            if flag != 0:
                break
        if flag != 0:
            print("Player X is the winner🚩🚩 ...")
            break
        userMove = False
    elif userMove == False:
        y = input("Player Y,enter the position : ").lower()
        if board[y]['value'] == ' ':
            board[y]['value']='o'
            movCounter+=1
        else:
            print("position already occupied")
            continue
        print(ticTacToe(board))
        list2.append(board[y]['pos']) 
        for winPos in winningPosition:
            counter = 0
            for individualPos in winPos:
                if individualPos in list2:
                    counter += 1
                if counter == 3:
                    flag = 1
                    break
            if flag != 0:
                break
        if flag != 0:
            print("Player Y is the winner🚩🚩 ...")
            break
        userMove = True
    if movCounter == 9:
        break
    
if flag != 0:
    print("Game Over")
else:
    print("Its A Draw !!")
