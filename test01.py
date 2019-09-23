def find(s,e,w):


N, E = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(E)]

minD = 1000000
find(0,4,0)