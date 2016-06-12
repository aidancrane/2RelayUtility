from relayinterface import *
ping([Q1],True)
time.sleep(1)
ping([Q2],True)
time.sleep(1)
ping([Q1,Q2],False)
time.sleep(1)
ping([Q2],True)
time.sleep(1)
ping([Q1],True)
time.sleep(1)


time.sleep(10)
GPIO.cleanup()