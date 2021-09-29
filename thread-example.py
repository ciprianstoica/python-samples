import threading, time, random


def action(a, b):
    current_thread = threading.currentThread()
    thread_name = current_thread.getName()
    print('Starting thread for: ', thread_name)
    time.sleep(random.randint(0, 15))
    print('Finished thread for: ', thread_name)
    print(a * b)

for arg in [(3, 5), (6, 8)]:
    t = threading.Thread(target=action, args=arg)
    t.start()

print("Continue processing...")