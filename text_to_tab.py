import os
import sys
from os.path import join
import codecs
import re

if len(sys.argv) > 1:
    path = sys.argv[1]
    if not os.path.exists(path):
        print('Error! Given path is not a valid directory.')
        exit()
else:
    print('Please provide the file-path argument.\n\nUsage: \npython text_to_tab.py /path/to/text/file/dirctory/\n')
    exit()

def spit():
    out_dir = os.path.join(path, 'outputs')
    try: 
        os.makedirs(out_dir)
    except OSError:
        if not os.path.isdir(out_dir):
            raise
    print "processing.."
    for root, sdirs, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename[-1] == '~' or 'outputs' in file_path:
                continue
            print file_path
            f = codecs.open(file_path, 'r', 'utf-8')
            nm = filename[:-4]+'_output.txt'
            wfile_path = os.path.join(root, 'outputs', nm)
            wf = codecs.open(wfile_path, 'w', 'utf-8')
            count = 0
            bd = ''
            temp = 1
            flag = True
            for line in f:
                count += 1
                if count == 1:
                    bd = line.strip().split(' ')
                    continue
                m = re.match('([0-9]+)([. ]*)([\W]+)', line)
                if m:
                    wf.write(bd[0]+'\t'+bd[1]+'\t'+m.group(1)+'\t'+m.group(3))
                else:
                    print 'This file couldn\'t be processed successfully!\n'
                    print
            wf.close()
            f.close()

spit()
