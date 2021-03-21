import threading


class Mythread(threading.Thread):
    def __init__(self, num_id, mutex, file, linhas):
        self.num_id = num_id
        self.mutex = mutex
        self.file = file
        self.total = []
        self.linhas = linhas
        threading.Thread.__init__(self)

    def inc_cont(self):
        self.cont += 1

    def run(self):
        for i in range(self.linhas):
            with self.mutex:
                line = self.file.readlines(1000)
                self.total.append([l.rstrip() for l in line])
                # print(self.cont)
        print(self.total)

    def ret_num(self):
        return self.total


with open('num.txt', 'r') as _file:
    mutex = threading.Lock()
    tds = []

    for i in range(1000):
        thread = Mythread(i, mutex, _file, 1000000)
        thread.start()
        tds.append(thread)

    for td in tds:
        td.join()
