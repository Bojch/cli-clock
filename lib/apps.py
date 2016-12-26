import subprocess
import time
from datetime import datetime

from lib.notification import notify
from lib.exceptions import PastTimeEnetredError

class timer:
    @staticmethod
    def run(sec, msg=None):
        while (sec > 0):
            sec -= 1
            time.sleep(1)

        notify("It's time", msg, sound=True)

    @staticmethod
    def init(sec, msg=None):
        msg = msg if msg else "This message should appear instantly, with a sound"

        subprocess.Popen(['nohup', './apps/timer.py', sec, msg])


class alarm:
    @staticmethod
    def run(at, msg=None):
        at = datetime.strptime(at, "%Y-%m-%d %H:%M")
        while(at > datetime.now()):
            time.sleep(0.200)

        notify("Wake up!", msg, sound=True)

    @staticmethod
    def init(at, msg=None):
        msg = msg if msg else "This message should appear instantly, with a sound"

        try:
            al = datetime.strptime(at, "%Y-%m-%d %H:%M")
            now = datetime.now()

            if now >= al:
                raise PastTimeEnetredError(at)

            subprocess.Popen(['nohup', './apps/alarm.py', at, msg])

        except ValueError as err:
            print "Wrong input!"
            print err
        except PastTimeEnetredError as ex:
            print "Time is up!"
            print "Entered '%s' time has to be in the future." % (ex.value)
