#number of lines you want in the new file
lines_per_file = 100000
smallfile = None
with open('/home/cantos/Downloads/index.jsonl') as bigfile: #give the file name and extension
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.jsonl'.format(lineno + lines_per_file)   #give the new file names and extension for smaller files
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()