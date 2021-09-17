#!/bin/bash
#
# Change setpoint so we have something to look at

while true
do
   caput training:setpoint 45
   sleep 120
   caput training:setpoint 25
   sleep 240
done
