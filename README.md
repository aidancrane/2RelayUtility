# 2RelayUtility
2RelayUtility allows you to test boards, aswell as gpio pins on a Raspberry Pi, In addition to being easy to setup, it also is written so that other functions can be used by importing the relayinterface file. oyoy shows an example of how this is possible. if you plan to use it for that purpose, then you do not need relaymaster as it is purely a gui.

In this instance I used

pin 1 for power (vcc). pin 6 for ground. pins 2 and 3 for IN1 and IN2.

Only tested on dual the relay board, however it should work on larger boards by swapping the wires for different relayws when testing (like changing IN1 to IN3) or rewriting the code, I have made this easier aswell by placing end and starting comments in blocks for each 'Module' for which i am refering to individual relays.

![pic of main menu](https://github.com/aidancrane/2RelayUtility/blob/master/relayscreenshot2.PNG)

![pic of turning off and on relays](https://github.com/aidancrane/2RelayUtility/blob/master/relayscreenshot2.PNG)

ttfn. Hope this helps.
