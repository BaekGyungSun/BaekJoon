H,M = map(int,input().split())

if 0 <= H < 24:
    if H == 0 and M < 45:
        H = H - 1 + 24
        M = M - 45 + 60
    elif 0 < H < 24 and M < 45:
        H -= 1
        M += 15
    else:
        M -= 45
print('{} {}'.format(H,M))