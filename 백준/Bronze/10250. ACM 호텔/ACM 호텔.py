T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    
    floor = (N-1) % H + 1
    room_number = (N-1) // H + 1
    print(f"{floor}{str(room_number).zfill(2)}")
