task_num = int(input())
for _ in range(task_num):
    cost = float(input())
    discount = 0.2
    print(f"${cost - (cost * discount):.2f}")