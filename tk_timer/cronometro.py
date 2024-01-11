import time

def cronometro():
    for num in range(10, 0, -1):
        time.sleep(1)
        print(num, end=' \r')
    print('fim')
    
cronometro()