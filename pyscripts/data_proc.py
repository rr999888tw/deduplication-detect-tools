import matplotlib.pyplot as plt
import statistics

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


def read_logfile(logfile, cache, isDedup, thresh):

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

x1, y1 = read_logfile('logs/logs-without-dedup-3', cache=False, isDedup=False, thresh=20)
x2, y2 = read_logfile('logs/log-without-dedup-2', cache=False, isDedup=False, thresh=20)
# x1, y1 = read_logfile('logs/log-without-dedup-2', True, False)

print (statistics.mean(y1))
print (statistics.mean(y2))

plt.plot(x1, y1, 'bo', x2, y2, 'ro')
plt.show()
