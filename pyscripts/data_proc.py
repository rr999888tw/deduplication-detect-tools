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

# 'logs/log-without-dedup-2'
# 'logs/logs-with-dedup-1'
# 'logs/logs-without-dedup-3'
# cache = True

# x4, y4 = read_logfile('vmlogs/vm04', cache=True, isDedup=True)
# x5, y5 = read_logfile('vmlogs/vm05', cache=True, isDedup=True)
# x6, y6 = read_logfile('vmlogs/vm06', cache=True, isDedup=True)
# x7, y7 = read_logfile('vmlogs/vm07', cache=True, isDedup=False)
# x8, y8 = read_logfile('vmlogs/vm08', cache=True, isDedup=False)
# x9, y9 = read_logfile('vmlogs/vm09', cache=True, isDedup=False)

x1, y1 = read_logfile('local-vmlogs/dedup-1', cache=True, isDedup=True)
x2, y2 = read_logfile('local-vmlogs/dedup-2', cache=True, isDedup=True)
x3, y3 = read_logfile('local-vmlogs/dedup-3', cache=True, isDedup=True)
x4, y4 = read_logfile('local-vmlogs/dedup-4', cache=True, isDedup=True)

x5, y5 = read_logfile('local-vmlogs/no-dedup-1', cache=True, isDedup=False)
x6, y6 = read_logfile('local-vmlogs/no-dedup-2', cache=True, isDedup=False)
x7, y7 = read_logfile('local-vmlogs/no-dedup-3', cache=True, isDedup=False)
x8, y8 = read_logfile('local-vmlogs/no-dedup-4', cache=True, isDedup=False)

print (statistics.mean(y1))
print (statistics.mean(y2))
print (statistics.mean(y3))
print (statistics.mean(y4))
print (statistics.mean(y5))
print (statistics.mean(y6))
print (statistics.mean(y7))
print (statistics.mean(y8))

print (np.corrcoef(x1, y1))
print (np.corrcoef(x2, y2))
print (np.corrcoef(x3, y3))
print (np.corrcoef(x4, y4))
print (np.corrcoef(x5, y5))
print (np.corrcoef(x6, y6))
print (np.corrcoef(x7, y7))
print (np.corrcoef(x8, y8))

# print (np.corrcoef(x4, y4))
# print (np.corrcoef(x5, y5))
# print (np.corrcoef(x6, y6))
# print (np.corrcoef(x7, y7))
# print (np.corrcoef(x8, y8))
# print (np.corrcoef(x9, y9))

# plt.plot(x1, y1, 'bo', x2, y2, 'ro')
# plt.show()
