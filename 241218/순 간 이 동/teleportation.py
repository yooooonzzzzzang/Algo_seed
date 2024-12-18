a,b,x,y = map(int,input().split())
# a -> b 
# a -> x -> y -> b
# a -> y -> x -> b 
print(min((abs(b-a), abs(x-a)+abs(b-y),  abs(y-a)+abs(b-x))))