import subprocess
import os
import sys
from os import listdir
from os.path import isfile, join

def get_files(datdir):
    
    onlyfiles = [datdir + '/' + f for f in listdir(datdir) if isfile(join(datdir, f))]
    onlyfiles.sort()
    return onlyfiles

datdir = sys.argv[1]
files = get_files(datdir)
binary = 'loadfile'

processes = []
for ele in files:
    p = subprocess.Popen(['./' + binary, ele])
    print(ele + " loaded ")
    processes.append(p)

print("files loaded...")
wait = input("PRESS ENTER TO CONTINUE.")

print("terminating the file loading...")
for p in processes:
    p.terminate()
print("terminated the file loading...")

# raw_input("all files loaded...")


# print(err)
# p.stdin.write(bytearray("echo cc > cc\n", "UTF-8"))
# time.sleep(1)
# print(p.stdout.read())


# import subprocess

# binary = "loadfile"
# p1 = subprocess.Popen(["./" + binary, "dat/data-16mb-21.dat"])
# print (p1.communicate("a\n"))

# p2 = subprocess.Popen(["/bin/sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(p2)
# p2.stdin = subprocess.PIPE
# p2.stdout = subprocess.PIPE
# p2.stderr = subprocess.PIPE
# out, err = p2.communicate(bytearray("echo aa > aa", 'UTF-8'))
# out, err = p2.communicate(bytearray("echo bb > bb", 'UTF-8'))

# print(p2.stdout.readline())
# print(out)


# process = subprocess.Popen(['echo', '"Hello stdout"'], stdout=subprocess.PIPE)
# stdout = process.communicate()[0]
# print ('STDOUT:{}'.format(stdout))