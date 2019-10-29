1. logs-with-dedup-1:
    Turn on the KSM.
    Open two identical VMs, wait for a period of time(1 hour).
    VM1 read 30 30MB files to its memory
    Test the memory write time on VM2.

2. log-without-dedup-2:
    Turn off the KSM.
    Open only one VM and test the memory write time

3. logs-without-dedup-3: 
    Turn on the KSM
    Didn't wait for a peirod of time(1 hour).
    VM1 stay idle
    Test the meomry write time on VM2.
    (not an accurate log, didn't wait for the merging to be stable)
