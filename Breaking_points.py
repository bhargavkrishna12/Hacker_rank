# Hacker Rank question on Breaking_points
n = input()
scores = list(map(int, input().split()))
b,w = scores[0],scores[0]
x,y = 0,0
for i in scores:
    if i>b:
        b=i
        x+=1
    if i<w:
        w=i
        y+=1
print("Best record :",x,"Worst Record :",y)
