import subprocess
import random
import time
from os import listdir
from os.path import isfile, join

def generate_a_log(binary, filename, filename2, logfilename="logs/log", interval=5, cache=True):
    retcode = -1
    if cache:
        retcode = subprocess.call(["./" + binary, "-1",  filename, "-2", filename2, "-i", str(interval), "-l", logfilename, "-c"])
    else:
        retcode = subprocess.call(["./" + binary, "-1",  filename, "-2", filename2, "-i", str(interval), "-l", logfilename])
    if retcode:
        args = [filename, filename2, logfilename, interval, cache]
        print("error info:\n", args)
        return
    else:
        return
    

def get_files(datdir):
    
    onlyfiles = [datdir + '/' + f for f in listdir(datdir) if isfile(join(datdir, f))]
    onlyfiles.sort()
    return onlyfiles

# def generate_logs(binary, filenames, logfilename, intervalRange, cache):
#     size = len(filenames)
#     return

def randPick2(arr):
    ret1 = random.choice(arr)
    ret2 = random.choice(arr)
    while (ret1 == ret2):
        ret2 = random.choice(arr)
    return (ret1, ret2)
    

if __name__ == '__main__':
    
    datdir = 'dat'
    files = get_files(datdir)
    logfilename = "logs/log1"
    interval = 5
    cache = True
    binary = "testdedup-single-auto"
    cmd_interval = 1
    intervalRange = range(3, 20, 1)
    cmd_intervalRange = range(1, 10, 1)
    exp_time = 100 # experiment time



    start = time.time()
    while True:
        filename, filename2 = randPick2(files)
        interval = random.choice(intervalRange)
        print ("interval = " + str(interval))
        generate_a_log(binary, filename, filename2, logfilename=logfilename, interval=interval, cache=cache)
        end = time.time()
        if(end - start >= exp_time):
            break
        else:
            sleepTime = random.choice( cmd_intervalRange )
            print("sleep = " + str(sleepTime))
            time.sleep(sleepTime)