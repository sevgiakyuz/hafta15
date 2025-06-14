import threading


def coder(number,number2):
    print(f'Coder ID: {number},{number2}')


threads = []
for k in range(1,5):
    for a in range(1,5):
        t = threading.Thread(target=coder, args=(k,a))
        threads.append(t)
        t.start()
