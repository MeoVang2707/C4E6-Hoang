from turtle import *
speed(-1)
color('red','yellow')
for n in range(9,2,-1):
    if n%2!=0:
        color('green','yellow')
    else:
        color('red','purple')
    begin_fill()
    for i in range(n):
        forward(100)
        left(180-180*(n-2)/n)
    end_fill()
mainloop()
