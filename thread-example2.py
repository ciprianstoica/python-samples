import threading, time, random


def action(a, b):
    current_thread = threading.currentThread()
    thread_name = current_thread.getName()
    print('Starting thread nr {} for: {}'.format(b,a))
    time.sleep(random.randint(0, 15))
    5 / (int(b) - 3)
    print('Finished thread nr {} for: {}: '.format(b,thread_name))


threads = []
index = 0
for f in ['source3.c', 'source2.c', 'source4.c', 'source1.c']:
    index += 1
    t = threading.Thread(target=action, name=f, args=(f, index))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

time.sleep(5)
print("Continue processing...")