from relayinterface import *
#
# ping(which relay(s)?,on?(true or false)?)
#

uniDict = {
'\\' : b'\xe2\x95\x9a',
'-'  : b'\xe2\x95\x90',
'/'  : b'\xe2\x95\x9d',
'|'  : b'\xe2\x95\x91',
'+'  : b'\xe2\x95\x94',
'%'  : b'\xe2\x95\x97',
}

def decode(x):
    return (''.join(uniDict.get(i, i.encode('utf-8')).decode('utf-8') for i in x))
def uiHead():
    print (chr(27) + "[2J")
    print (decode(" +----------------------------------------------------------------------------%"))
    print (decode(" | Aidan's Relay Utility                                                      |"))
    print (decode(" |                                                                            |"))
    print (decode(" |                                                                            |"))
    print (decode(" |                                                                            |"))
    print (decode(" |                                                                            |"))
def uiFoot():
    print (decode(" |                                                                            |"))
    print (decode(" |                                                                            |"))
    print (decode(" |                                                                            |"))
    print (decode(" |                                                                            |"))
    print (decode(" |                                                                            |"))
    print (decode(" |                                                                            |"))
    print (decode(" |                                                                            |"))
    print (decode(" | 1 . Get the status of the relay switches.                                  |"))
    print (decode(" | 2 . Set the status of the relay switches.                                  |"))
    print (decode(" | 3 . Clear the relay switches, with a short pulse.                          |"))
    print (decode(" | 4 . GPIO Cleanup.                                                          |"))
    print (decode(" | 5 . Exit.                                                                  |"))
    print (decode(" |                                                                            |"))
    print (decode(" | c . View credits                                                           |"))
    print (decode(" \\----------------------------------------------------------------------------/"))
uiHead()
print (decode(" |                                                                            |"))
print (decode(" |                                                                            |"))
uiFoot()

while True:

    try:
            ### MAIN

            response = raw_input("")
            if response == 'c':
                uiHead()
                print (decode(" |") + ("    https://youtu.be/oaf_zQcrg7g ") + decode("  <- Initial inspiration and abstract      |"))
                print (decode(" |") + ("    https://github.com/skiwithpete ") + decode("<- Initial starting point                |"))
                print (decode(" |    A guy on stackoverflow wrote the dictionary for the windows             |"))
                print (decode(" |    but I cant find who it was, but thanks to him also.                     |"))
                print (decode(" |                                                                            |"))
                print (decode(" |") + ("    https://infinityflame.co.uk  ") + decode("  <- Made by Aidan Crane in 2016           |"))
                print (decode(" |                                                                            |"))
                print (decode(" | 1 . Get the status of the relay switches.                                  |"))
                print (decode(" | 2 . Set the status of the relay switches.                                  |"))
                print (decode(" | 3 . Clear the relay switches, with a short pulse.                          |"))
                print (decode(" | 4 . GPIO Cleanup.                                                          |"))
                print (decode(" | 5 . Exit.                                                                  |"))
                print (decode(" |                                                                            |"))
                print (decode(" | c . View credits                                                           |"))
                print (decode(" \\----------------------------------------------------------------------------/"))
            elif response == '5':
                uiHead()
                print (decode(" |  GoodBye!                                                                  |"))
                print (decode(" \\----------------------------------------------------------------------------/"))
                if QSTAT[0] or QSTAT[1] == True:
                    GPIO.cleanup()
                break
            elif response == '4':
                GPIO.cleanup()
                uiHead()
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                uiFoot()
            elif response == '1':
                print(chr(27) + "[2J")
                uiHead()
                print (decode(" |          Okay!                                                             |"))
                if QSTAT[0] == False:
                    responseA = "is off"
                else:
                    responseA = "is on "
                if QSTAT[1] == False:
                    responseB = "is off"
                else:
                    responseB = "is on "
                print (decode(" |          It looks to me like, Relay1 ") + responseA + (", and Relay2 ") + responseB + decode(".            |"))
                uiFoot()
            elif response == '2':
                print(chr(27) + "[2J")
                uiHead()
                print (decode(" |          Okay!                                                             |"))
                print (decode(" |          Tell Me which relay you would like to set                         |"))
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                print (decode(" |  1 . Relay 1 to On                                                         |"))
                print (decode(" |  2 . Relay 2 to On                                                         |"))
                print (decode(" |  3 . Relay 1 to Off                                                        |"))
                print (decode(" |  4 . Relay 2 to Off                                                        |"))
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                print (decode(" \\----------------------------------------------------------------------------/"))
                newInput = raw_input("")
                if newInput == '1':
                    ping([Q1],True)
                if newInput == '2':
                    ping([Q2],True)
                if newInput == '3':
                    ping([Q1],False)
                if newInput == '4':
                    ping([Q2],False)
                uiHead()
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                uiFoot()
            elif response == '3':
                uiHead()
                print (decode(" |          Okay!                                                             |"))
                print (decode(" |          Pulsing for 15 seconds, then clearing. Make sure to remove power  |"))
                uiFoot()
                
                #
                # This is just a little testing sequence
                # You are prompted to remove power to prevent damage
                # to the electrical items on the end of the relay such
                # as a lamp.
     
                ping([Q1,Q2],True)
                time.sleep(1)
                ping([Q1,Q2],False)
                time.sleep(1)
                ping([Q1,Q2],True)
                time.sleep(1)
                ping([Q1,Q2],False)
                time.sleep(1)
                ping([Q1],True)
                time.sleep(0.5)
                ping([Q2],True)
                time.sleep(0.5)
                ping([Q1],False)
                time.sleep(0.5)
                ping([Q2,Q1],False)
                for i in range(4):
                     ping([Q1,Q2],True)
                     time.sleep(0.5-i/4)
                     ping([Q1,Q2],False)
                     time.sleep(0.5-i/4)
                ping([Q1],True)
                time.sleep(0.25)
                ping([Q1],False)
                time.sleep(0.25)
                ping([Q1],True)
                time.sleep(0.25)
                ping([Q1],False)
                time.sleep(0.25)
                ping([Q1],True)
                time.sleep(0.25)
                ping([Q1],False)
                time.sleep(0.25)
                ping([Q2],True)
                time.sleep(0.25)
                ping([Q2],False)
                time.sleep(0.25)
                ping([Q2],True)
                time.sleep(0.25)
                ping([Q2],False)
                time.sleep(0.25)
                ping([Q2],True)
                time.sleep(0.25)
                ping([Q2],False)
                time.sleep(0.25)
            else:
                uiHead()
                print (decode(" |                                                                            |"))
                print (decode(" |                                                                            |"))
                uiFoot()
            
            if QSTAT[0] or QSTAT[1] == True:
                if newInput == None:
                    GPIO.cleanup()
                    newInput = None
            response = None
            ### END MAIN
            
    except KeyboardInterrupt:
            uiHead()
            print (decode(" |  GoodBye!                                                                  |"))
            print (decode(" \\----------------------------------------------------------------------------/"))
            if QSTAT[0] or QSTAT[1] == True:
                GPIO.cleanup()
            break

    # Q1 On Q2 Off /
    # Q1 On Q2 On /
    # Q1 Off Q2 On /
    # Q1 On Q2 On /
    # Q1 Off Q2 On /
    # Q1 Off Q2 Off /
