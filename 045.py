
nt = 285
np = 165
nh = 143
T = P = H = 40755
while 1:
    nh += 1
    H = nh*(2*nh-1)
    while P < H:
        np += 1
        P = np*(3*np - 1)//2
    while T < H:
        nt += 1
        T = nt*(nt + 1)//2
    if P == H and T == H:
        print(P)
        break
