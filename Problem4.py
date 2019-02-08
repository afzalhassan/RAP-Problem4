#  4. Develop a program to calculate the total and individual player scores in a cricket match. 
#  Input would be an array with the index representing the ball number and the value representing the runs scored of that ball.
#  
#  Assumptions/Tips:
#  1.	No Extras bowled
#  2.	Batsman has to be rotated after ever over
#  3.	Bowler can bowl any number of overs
#  4.	Assume Batsman 1 is on strike for the first ball.

player1 = []
player2 = []

flag1 = 1
flag2 = 0
lst = list(map(int,input().split()))
for i in range(len(lst)):
    if flag1 is 1:
        a = 0
        player1.append(lst[i])
        if lst[i]%2 is 0:
            flag2,flag1 = 0,1
        if lst[i]%2 is 1:
            flag1,flag2= 0,1
    elif flag2 is 1:
        a = 1
        player2.append(lst[i])
        if lst[i]%2 is 0:
            flag1,flag2= 0,1
        if lst[i]%2 is 1:
            flag2,flag1 = 0,1
    if (i+1)%6 is 0:
        if a is 1:
            if player2[-1]%2 is 1:
                flag1,flag2= 0,1
            else:
                flag2,flag1 = 0,1
        else:
            if player1[-1]%2 is 1:
                flag2,flag1 = 0,1
            else:
                flag1,flag2= 0,1
				
print ("Total Score:",sum(lst))
print ("Batsman 1 Score : ",sum(player1),"(",end="")
print (' + '.join([str(score) for score in player1 if score > 0]),end="")
print (")")
print ("Batsman 2 Score : ",sum(player2),"(",end="")
print (' + '.join([str(score) for score in player2 if score > 0]),end="")
print (")")
