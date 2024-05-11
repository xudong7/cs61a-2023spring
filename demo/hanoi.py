import time

def hanoi(n):
    def move(n, source, target, using):
        if n:
            move(n - 1, source, using, target)
            print('Move disk from', source, 'to', target)
            move(n - 1, using, target, source)
    move(n, 'A', 'C', 'B')

start = time.time()
hanoi(20)
end = time.time()
print(end - start)

# another solution
# def move(n, start, end):
#     print(f'Move disk {n} from {start} to {end}')    

# def hanoi(n, start, end):
#     if n == 1:
#         move(n, start, end)
#     else:
#         spare = 6 - start - end
#         hanoi(n-1, start, spare)
#         move(n, start, end)
#         hanoi(n-1, spare, end)

# hanoi(3, 1, 3)