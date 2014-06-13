#!/usr/bin/env python

#
# trafficlog.py		Data logging from WSDOT API
# version		0.1.1
# author		Brian Walter @briantwalter
# description		Record average and current traffic times from
#			Seattle to Bellevue to establish baselines

# imports
import time
import datetime
import requests
from daemon import runner
from  ConfigParser import SafeConfigParser

# configs
config = SafeConfigParser()
config.read('config.py')
csvfile = config.get('trafficlog', 'csvfile')
logfile = config.get('trafficlog', 'logfile')
pidfile = config.get('trafficlog', 'pidfile')
apiurl = config.get('trafficlog', 'apiurl')
apikey = config.get('trafficlog', 'apikey')
url = apiurl + apikey

def main():
  # loop forever checking every 5 minutes
  while True:
    # GET the url
    response = requests.get(url)
    # load the JSON response to a data object
    data = response.json()
    # open the csv file in append mode
    file = open(csvfile, "a")
    # parse updated time
    ts = str(data['TimeUpdated'])
    # need to strip off tz and extra characters from the data to get epoch
    head = 'Date('
    # known issue --> not daylight savings friendly
    tail = '-0700'
    # grab string as epoch time stamp here
    ets = ts[ts.find(head)+len(head):ts.rfind(tail)]
    # get a human readable time stamp
    hts = datetime.datetime.fromtimestamp(float(ets)/1000.).strftime('%Y-%m-%d,%H:%M:%S')
    # build a row to enter in the file
    row = str(data['Description']) + "," + hts + "," + str(data['AverageTime']) + "," + str(data['CurrentTime']) + "\n"
    # write the row to the file
    file.write(row)
    # close the file don't leave it open in between intervals
    file.close()
    # go to sleep
    time.sleep(300)	# check every 5 minutes

# daemon properties
class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = logfile
        self.stderr_path = logfile
        self.pidfile_path =  pidfile
        self.pidfile_timeout = 5
    def run(self):
        main()

# execute the app according to argument
app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
