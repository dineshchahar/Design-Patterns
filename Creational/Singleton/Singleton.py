from threading import Thread, Lock
import time
class Singleton(type):
    _instances = {} # dictionary to hold the instance of the class, this is metaclass level attribute/variable.
    _lock = Lock() # to make it thread safe.
    def __call__(self, *args, **kwargs): # here is self is the class itself not the instance.
        with self._lock:
            if self not in self._instances:
                instance = super().__call__(*args,**kwargs)
                self._instances[self] = instance
                time.sleep(1) # to simulate some resource intensive task.
            return self._instances[self]

class NetworkDriver(metaclass = Singleton):
    def log(self):
        print(f"{self}\n")
        
def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton


if __name__ == '__main__':
    # single thread
    # s1 = create_singleton() 
    # s2 = create_singleton()

    # multithread
    p1 = Thread(target=create_singleton)
    p2 = Thread(target=create_singleton)

    p1.start()
    p2.start()

"""
without the lock , there is a race condition here and two instances will be created. With two threads, both can run the if self not in ... check before either one stores the instance, so both threads create an object.
to make it thrad safe , we need to use the locks around the instance creation code.
"""