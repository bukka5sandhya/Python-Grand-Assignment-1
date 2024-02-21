A = int(input())#4(input) #3(another input)
B = int(input()) #4(input) #2(another input)
C = int(input()) #4(input) #3(another input)

if A == B == C:
    print("Equilateral")
elif (A==B) or (B==C) or (A==C):
    print("Isosceles")
elif A!=B!=C:
    print("Scalene")
