import multiprocessing
import uuid

class ProcessTest(multiprocessing.Process):
    def run(self):
        unique_filename = str(uuid.uuid4())
        f = open(unique_filename, "w+")
        f.write("run method from: %s" %self.name + "\n")
        f.close()
        return

if __name__ == '__main__':
    jobs = []

    for i in range(5):
        p = ProcessTest()
        jobs.append(p)
        p.start()
        p.join()