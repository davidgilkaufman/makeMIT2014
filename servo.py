import sys
sys.path.append("lib/pythonArduino")
import time

import arduino

# A simple example of using the arduino library to
# control a servo.

ports=[9,10]#,11]
starts=[20,20,20]
ends=[40,40,40]
delay = 0.25

ard = arduino.Arduino()
servos = [arduino.Servo(ard, p) for p in ports] # Create servo objects
ard.run()  # Run the Arduino communication thread

try:
  while True:
    for i in xrange(len(servos)):
      servos[i].setAngle(starts[i])
    print "Start"
    time.sleep(delay)
    for i in xrange(len(servos)):
      servos[i].setAngle(ends[i])
    print "End"
    time.sleep(delay)
except:
  ard.stop()

