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
    for i in range(100):
        generate_big_random_bin_file("dat-own/data-32mb-" + str(i) + ".dat-own",1024*1024*32)