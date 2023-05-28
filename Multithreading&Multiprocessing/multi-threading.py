import threading
import time

def sleep_func(seconds):
    print("Sleeping for {} seconds".format(seconds))
    time.sleep(seconds)

t1=time.perf_counter();
# Normal code
# sleep_func(5)
# sleep_func(3)
# sleep_func(2)

# using threading
thread1=threading.Thread(target=sleep_func,args=[5])
thread2=threading.Thread(target=sleep_func,args=[3])
thread3=threading.Thread(target=sleep_func,args=[2])


thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
t2=time.perf_counter();
print(t2-t1)