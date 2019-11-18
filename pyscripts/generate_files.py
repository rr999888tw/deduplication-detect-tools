import sys
import os

def generate_big_random_bin_file(filename,size):
    """
    generate big binary file with the specified size in bytes
    :param filename: the filename
    :param size: the size in bytes
    :return:void
    """
    import os 
    with open('%s'%filename, 'wb') as fout:
        fout.write(os.urandom(size)) #1

    print ('big random binary file with size %f generated ok'%size)
    pass

if __name__ == '__main__':
    dirname = sys.argv[1]
    try:
        os.mkdir(dirname)
    except:
        print(dirname + ' creation error \n')

    for i in range(100):
        generate_big_random_bin_file( dirname + "/data-32mb-" + str(i) + ".dat",1024 * 1024 * 32)