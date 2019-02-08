import random 

def the_board(): 
    for i in range(0,9,3): 
        print(board[i] + "|" + board[i+1] + "|" + board[i+2]) 
        if i == 6: 
            break 
        print("-+-+-") 

    print("--------------") 

def strong(times): 
    for i in range(times,times+2): 
        if i % 2 == 0: 
            mark = "o" 
        else: 
            mark = "x" 
      
    for pattern in winning_patterns: 
        board_line = list(board[j] for j in pattern) 
        if board_line == [" ",mark,mark] or \
            board_line == [mark," ",mark] or \
            board_line == [mark,mark," "]: 
            for k in pattern: 
                 if board[k] == " ": 
                    return k 

    return random.randint(0,8) 

def turn(times,number): 
    if board[number] != " ": 
        if times % 2 == 0: 
            print("NG") 
            num = int(input("数字を再入力:")) 
            return turn(times,num) 
        else: 
            num = random.randint(0,8) 
            return turn(times,num) 

    if times % 2 == 0: 
        board[number] = "o" 
    else: 
        board[number] = "x" 

def judge():
    for pattern in winning_patterns: 
        if set([board[i] for i in pattern]) == {"o"}: 
            return True 
        elif set([board[i] for i in pattern]) == {"x"}: 
            return True 

player_name = input("三目並べを始めます。名前を入力:") 
name = [player_name,"computer"] 
winning_patterns = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] 
board = [str(i) for i in range(9)] 

the_board() 
board = [" " for i in range(9)] 
the_board() 

for i in range(9): 
    print(name[i % 2] + "のターン") 
    
    if i % 2 == 0: 
        num = int(input("数字を入力:")) 
    else: 
        num = strong(i)

    turn(i,num) 
    the_board() 

    if judge() == True: 
        print(name[i % 2] + "の勝利です") 
        break 

    if i == 8: 
        print("引き分けです") 

print("THE END")
