from subprocess import check_call as cc

for i in range(0, 5):
    cc(['./process.sh', str(i+1)])

