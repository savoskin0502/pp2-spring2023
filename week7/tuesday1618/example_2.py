fpath = './rawdata.txt'
f = open(fpath, mode='w')
f.write('hello from kbtu\n')  # \n; \r; \r\n;
f.write('hello from kbtu')
f.close()
