import matplotlib.pyplot as plt
import statistics
import numpy as np

class Entry:
    
    def __init__(self, timeNeeded, fileSize, isDedup, interval, cache,  **kwargs):
        self._timeNeeded = timeNeeded
        self._fileSize = fileSize
        self._isDedup = bool(isDedup)
        self._interval = interval
        self._cache = bool(cache)
        # self.r = realpart
        # self.i = imagpart
        return

    def attribute(self):
        return self.__dict__

    def isDedup(self):
        return (self._isDedup)
    
    def isCache(self):
        return (self._cache)
    
    def get_timeNeeded(self):
        return self._timeNeeded
    
    def get_interval(self):
        return self._interval

def parseEntry(entryStr):

    args = dict()
    for ele in entryStr.strip().split("  "):

        if '=' in ele:
            tmp = ele.split('=')
            if (tmp[1].isdigit()):
                args[tmp[0]] = float(tmp[1])
            else:
                args[tmp[0]] = tmp[1]

        else:
            args['timeNeeded'] = float(ele)
    return (args)


def read_logfile(logfile, cache, isDedup, thresh=1000):

    f = open(logfile).read()
    arr = f.strip().split('\n')
    
    dataArr = []
    for ele in arr:
        argDic = parseEntry(ele)
        entry = Entry(**argDic, isDedup=isDedup)
        if entry.isCache() == cache and entry.get_interval() < thresh:
            dataArr.append(entry)
    
    x = list (map(lambda entry: entry.get_interval(), dataArr) )
    y = list (map(lambda entry: entry.get_timeNeeded(), dataArr))
    return (x, y)

def plot(filename, title, cache=True, isDedup=True):
    xi, yi = read_logfile(filename, cache, isDedup)

    x = np.linspace(min(xi), max(xi), 1000)
    cor = np.corrcoef(xi, yi)[0][1]
    x0 = statistics.mean(xi)
    y0 = statistics.mean(yi)
    sigx = statistics.stdev(xi)
    sigy = statistics.stdev(yi)
    m = cor * sigy / sigx
    print(" m = ", m)
    b = y0 - m * x0
    y = [m * ele + b for ele in x]
    plt.plot(xi, yi, 'bo')
    plt.plot(x, y, linestyle='solid', color="red")
    plt.xlabel("waiting time (s)")
    plt.ylabel("write access time ")
    plt.title(title)
    plt.legend(['single attempt', "w = {} * t + {}".format( int(m), '{:.2e}'.format(b))])
    plt.savefig("fig/{}".format(title))

plt.figure(1)
plot('local-vmlogs/dedup-2', "local, dedup")

plt.figure(2)
plot('local-vmlogs/no-dedup-6', "local, no dedup")

plt.figure(3)
plot('vmlogs/vm08', "aws C5")


plt.show()

# plt.figure(1)
# plot('vmlogs/vm04')

# plt.figure(2)
# plot('vmlogs/vm05')

# plt.figure(3)
# plot('vmlogs/vm06')

# plt.figure(4)
# plot('vmlogs/vm07')

# plt.figure(5)
# plot('vmlogs/vm08')

# plt.figure(6)
# plot('vmlogs/vm09')


"logs/logs-with-dedup-1"
"logs/logs-without-dedup-1"
"logs/logs-without-dedup-2"
"logs/logs-without-dedup-3"

'vmlogs/vm04'
'vmlogs/vm05'
'vmlogs/vm06'
'vmlogs/vm07'
'vmlogs/vm08'
'vmlogs/vm09'

'local-vmlogs/dedup-1'
'local-vmlogs/dedup-2'
'local-vmlogs/dedup-4'
'local-vmlogs/no-dedup-1'
'local-vmlogs/no-dedup-2'
'local-vmlogs/no-dedup-4'
'local-vmlogs/no-dedup-6'