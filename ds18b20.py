#!/usr/bin/python

def gettemp(sensor):
        f = open('/sys/bus/w1/devices/{0}/w1_slave'.format(sensor),'r')
        l1 = f.readline()
        l2 = f.readline()
        temp = l2.split('t=',1)
        f.close()
        return int(temp[1])

if __name__ == '__main__':
    print '{0}'.format(gettemp('28-0417504372ff')/float(1000))
