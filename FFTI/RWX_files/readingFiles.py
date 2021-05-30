file = open('./inputFile.txt', 'r')
approvedFile = open('./approvedFile.txt', 'w')
failFile = open('./failFile.txt', 'w')

for line in file:
    pass_the_test = line.split()
    if pass_the_test[2] == 'P':
        approvedFile.write(line)
    elif pass_the_test[2] == 'F':
        failFile.write(line)

file.close()
approvedFile.close()
failFile.close()
