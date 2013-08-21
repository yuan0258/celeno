# Purpose: stress 100 times the firmware upgrade over SPW102BridgeV3 in Web GUI
#!/usr/bin/env python
import requests
import time
i=0
runs=0
test_cycles=100

#http://192.168.0.21/hcti_laden_firm.asp
#192.168.0.21/cgi-bin/upload_sw_update.cgi
device_ip="192.168.0.21"
url = "http://" + device_ip + "/cgi-bin/upload_sw_update.cgi"
FW ="SPW102V3Bridge_6.46.143_v001.047.093_ap_Upload_Bundle_image_svn9544.bin.xor"

while runs <= test_cycles:
    i=0
    print 'Current runs = ' + str(runs)
    runs = runs + 1
    #Please see the source code in hcti_laden_firm.asp
    files = {'FIRM_DAT': open(FW, 'rb')}
    r = requests.post(url, files=files)
    print r.text
    while 1:
        time.sleep(1)
        i=i+1
        #print 'Wait upgrade firmware ' + str(i) + ' sec'
        #Wait after f/w upgrading in 3 mins
        if i == 180:
	    break

