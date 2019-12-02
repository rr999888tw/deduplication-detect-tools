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

def plot(filename, cache=True, isDedup=True):
    xi, yi = read_logfile(filename, cache, isDedup)

    x = np.linspace(min(xi), max(xi), 1000)
    cor = np.corrcoef(xi, yi)[0][1]
    x0 = statistics.mean(xi)
    y0 = statistics.mean(yi)
    sigx = statistics.stdev(xi)
    sigy = statistics.stdev(yi)
    m = cor * sigy / sigx
    b = y0 - m * x0
    y = [m * ele + b for ele in x]
    plt.plot(xi, yi, 'ro')
    plt.plot(x, y, linestyle='solid')
    # plt.show()

plt.figure(1)
plot('local-vmlogs/dedup-2', True)

plt.figure(2)
plot('local-vmlogs/no-dedup-4', True)

plt.show()

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