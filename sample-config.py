#
# config.py		Settings for Py-Traffic*
# version		0.0.1
# author		Brian Walter @briantwalter
# description		For use with ConfigParser module (INI format)
#			

[trafficlog]
csvfile: /tmp/trafficlog.csv
logfile: /tmp/trafficlog.log
pidfile: /tmp/trafficlog.pid
apikey: XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXXXXXXX	# Insert your WSDOT API key here
apiurl: http://www.wsdot.wa.gov/Traffic/api/TravelTimes/TravelTimesREST.svc/GetTravelTimeAsJson?TravelTimeID=96&AccessCode=

[trafficlcd]
logfile: /tmp/trafficlcd.log
pidfile: /tmp/trafficlcd.pid
apikey: XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXXXXXXX	# Insert your WSDOT API key here
apiurl: http://www.wsdot.wa.gov/Traffic/api/TravelTimes/TravelTimesREST.svc/GetTravelTimeAsJson?TravelTimeID=96&AccessCode=
