#!/usr/bin/python

from time import sleep
import ds18b20
import logging
import db

def run():
    print "starting temp service..."
    try:
        while True:
            t = ds18b20.gettemp('28-0417504372ff')
            print t
            db.write(t)
            sleep(10)
    except KeyboardInterrupt, e:
        logging.info("Starting temp stopping...")

if __name__ == '__main__':
    run()
