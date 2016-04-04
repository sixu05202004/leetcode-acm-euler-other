# Read from the file file.txt and output the tenth line to stdout.
awk -F:"\n" '{if(NR==10) {print}}' file.txt