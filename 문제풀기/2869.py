import math

A, B, V = map(int, input().split())

answer = (V - B) / (A - B)

print(math.ceil(answer))
