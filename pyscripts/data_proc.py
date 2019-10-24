class Entry:
    
    def __init__(self, timeNeeded, fileSize, isDedup, interval, cache,):
        self._timeNeeded = timeNeeded
        self._fileSize = fileSize
        self._isDedup = isDedup
        self._interval = interval
        self._cache = cache
        # self.r = realpart
        # self.i = imagpart
        return

    def isDedup(self):
        return (self._isDedup)
    
    def isCache(self):
        return (self._cache)

def parseEntry(entryStr):

    args = dict()
    for ele in ent.strip().split("  "):

        if '=' in ele:
            tmp = ele.split('=')
            if (tmp[1].isdigit()):
                args[tmp[0]] = float(tmp[1])
            else:
                args[tmp[0]] = tmp[1]

        else:
            args['timeNeeded'] = float(ele)

    # print(args)
    return Entry(**args)
    
    # return Entry()

ent = "timeNeeded=2019666.44  filename=dat/data-16mb-19.dat  filename2=dat/data-16mb-62.dat  interval=9  cache=1"
print(parseEntry(ent))

# log_Without_dedup = open("logs/log1", "r").read().strip()
# print((log_Without_dedup.split("\n")))