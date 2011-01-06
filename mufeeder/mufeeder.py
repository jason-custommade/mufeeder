#!/usr/bin/env python
###############################################################################
#                                                                             #
# Mu-Feeder, A Free Software program to p st RSS feeds to your microblog.     # 
# Copyright (C) 2009  Robert Connolly <rob@webworxshop.com>                   #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU Affero General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or           #
# (at your option) any later version.                                         #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU Affero General Public License for more details.                         #
#                                                                             #
# You should have received a copy of the GNU Affero General Public License    #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
###############################################################################

from services import statusnet
import urllib2
import sys

# simplejson is used in python versions before 2.6
try:
	import json
except ImportError:
	import simplejson as json

# attempt to load the settings file
try:
	import settings
except ImportError:
	print "ERROR: Can't import settings.py, please create this file!"
	sys.exit(1)

def post_status(plan, user, amt):
	# import service
	try:
		service =  statusnet.Service()
	except ImportError:
		print "ERROR: Unknown service type '" + settings.ACCOUNT_TYPE + "'"
		return 1
	msg = '!sales ' + str(plan) + ' has been sold by ' + user.username + ' for $' + str(amt)	
        service.post(msg)
	return 0
