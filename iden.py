#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5

G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"

from multiprocessing.pool import ThreadPool
import requests as r
import json
import sys
import os

def iden(hes):
	api=r.get('https://ostch.herokuapp.com/api/v1/hash-identifier?hash='+hes).text
	js=json.loads(api)
	print '%s[ %sHASH %s] %s'%(W0,Y0,W0,hes)
	if js['hash_type'] == 'unknown':
		print '%s[ %sTYPE %s] UNKNOWN'%(W0,R0,W0)
	else:
		print '%s[ %sTYPE %s] %s'%(W0,G0,W0,js['hash_type'])
		open('results.txt','a+').write(hes+' => '+js['hash_type']+'\n')
	print

try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s   _ __                                    _
  /// / _   __  /7   () _// __ _    /7 (),'_7() __ _
 / ` /,'o| (c' / \  /7,'o/,'o// \/7/_7/7/_7 /7,'o///7
/_n_/ |_,7/__)/n_/ //|__/ |_(/_n_/// ////  // |_(//

%s[%s>%s] Powered by https://ostch.herokuapp.com
%s[%s>%s] Coded by D4RKSH4D0WS
'''%(C1,W0,G0,W0,W0,G0,W0)
	ThreadPool(5).map(iden,open(sys.argv[1]).read().splitlines())
	print '%s[ %sDONE %s] %sSaved in results.txt'%(W1,G1,W1,W0)
except r.exceptions.ConnectionError:
        exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
        exit('%s[%s!%s] %sUse : python2 %s hash.txt'%(W1,R1,W1,W0,sys.argv[0]))
except IOError:
        exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
        exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))
