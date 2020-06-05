import threading, queue
class Multithreading:
    def multithreading(self, num,q):

        result = f"The cube of {num} is {num * num * num}"
        q.put(result)


if __name__ == "__main__":
    q = queue.Queue
    t1 = threading.Thread(target=Multithreading().multithreading, args=(10,q))
    t2 = threading.Thread(target=Multithreading().multithreading, args=(10,q))
    print(t1.get())
    t1.start()
    t2.start()

    t1.join()
    t2.join()


