a =str(input()) #Scissor(input)
b = str(input()) #Rock(input)

if ((a == "Paper") & (b == "Rock")) | ((a == "Scissor") & (b == "Paper")) | ((a == "Rock") & (b == "Scissor")):
    print("Abinav Wins")
elif ((b == "Paper") & (a == "Rock")) | ((b == "Scissor") & (a  == "Paper")) | ((b == "Rock") & (a == "Scissor")):
    print("Anjali Wins")
elif (a == b):
    print("Tie")