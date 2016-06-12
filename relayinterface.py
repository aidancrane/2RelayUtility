#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# A stupid way to shorten some words to save on effort when typing this out
Q1 = "RELAY1"
Q2 = "RELAY2"

#
# Q Stat is the tracking list for when we want to check that relays are on or off
# I have done it this way because it means we dont have to change modes on the GPIO
#
QSTAT = [False,False]
setup = False
def setupPins():
    setup = True
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT) 
    GPIO.output(2, GPIO.HIGH)
    GPIO.setup(3, GPIO.OUT) 
    GPIO.output(3, GPIO.HIGH)

setupPins()
def ping(relaysInvolved,on):
    #
    # Check that the pins are configured, becuase sometimes in the code
    # ping is reffered to before and that seemed to cause bugs
    #
    #
    if setup != True:
        setupPins()

    try: 
        # Start Module 1
        if Q1 in relaysInvolved:
            if on == False:
                GPIO.output(2, GPIO.HIGH)
                QSTAT[0] = False
                if QSTAT[1] == True:
                    GPIO.output(3, GPIO.LOW)
            if on == True:
                GPIO.output(2, GPIO.LOW)
                QSTAT[0] = True
                if QSTAT[1] == True:
                    GPIO.output(3, GPIO.LOW)

        # End Module 1

    #
    #  The Code is setup in modules to allow easy expansion
    #  simply add another one for expansion
    #  I only have a 2 relay board so from here http://www.ebay.co.uk/itm/351049866976
    #  but it could be used for 16 or larger relays
    #

    # Start Module 2
        if Q2 in relaysInvolved:
            if on == False:
                GPIO.output(3, GPIO.HIGH)
                QSTAT[1] = False
                if QSTAT[0] == True:
                    GPIO.output(2, GPIO.LOW)
            if on == True:
                GPIO.output(3, GPIO.LOW)
                QSTAT[1] = True
                if QSTAT[0] == True:
                    GPIO.output(2, GPIO.LOW)
    except:
        excep ("Something bad went wrong")
