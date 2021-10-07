import math

D, H, W = map(int, input().split())

# H : W = x : y
# x**2 + y**2 == D**2

# Wx = Hy. y = Wx/H
# x**2 + (W**2*x**2)/H**2 = D**2

x = math.sqrt((D**2)*(H**2)/(H**2+W**2))
y = W*x/H

print(math.floor(x), math.floor(y))
