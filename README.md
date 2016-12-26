# Simple Cli Clock

Simple clock with timer and alarm to fire osX notifications.

# Installation

You want to install PyObj https://pythonhosted.org/pyobjc/install.html

Make this files executable clock, apps/alarm, apps/timer and you achieve it with the command:

  chmod a+x <file-name>

# How to use it?  
  ./clock [-h] [-t] [-s] [-m] {alarm,timer}

  -h, --help     Show this help message and exit.
  -t, --time     Format: Y-m-d h:i [2016-07-22 12:33]
  -s, --sec
  -m, --msg      The message you want to get from notification.

## Alarm example
Use the future time as passed argument.

  ./clock alarm -t '2016-07-22 12:33' -m "Meeting is starting in 10 min!"

## Timer example
Count down n seconds.

  ./clock timer -s 10
