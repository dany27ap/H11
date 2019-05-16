import multiprocessing
import time


class ProcessTest(multiprocessing.Process):

    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.__semafor = Semaphore(1)

    def run(self):
        self.__semafor.rosu()
        open("text.txt", "a").write("Lab PP" + "\n")
        self.__semafor.verde()
        return


class Semaphore:
    def __init__(self, n):
        self.__n = n

    def rosu(self):
        while self.__n <= 0:
            time.sleep(0.1)
            self.__n -= 1

    def verde(self):
        self.__n += 1



if __name__ == '__main__':
    jobs = []

    for i in range(5):
        p = ProcessTest()
        jobs.append(p)
        p.start()
        p.join()

