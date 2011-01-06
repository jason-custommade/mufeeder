###############################################################################
#                                                                             #
# Mu-Feeder, A Free Software program to post RSS feeds to your microblog.     # 
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
import sys
import urllib, urllib2

try:
	import json
except ImportError:
	import simplejson as json

try:
	from mufeeder import settings
except ImportError:
	print "ERROR: Can't import settings.py, please create this file!"
	sys.exit(1)

class Service(object):

	def __init__(self):
		#print "Using server: " + self.server
		pass

	def post(self, msg):
		url = "https://" + self.server + "/statuses/update.json"
		
		auth_handler = urllib2.HTTPBasicAuthHandler(urllib2.HTTPPasswordMgrWithDefaultRealm())
		auth_handler.add_password(None, url, settings.ACCOUNT_LOGIN, settings.ACCOUNT_PASSWORD)
		opener = urllib2.build_opener(auth_handler)
		urllib2.install_opener(opener)
		
		data = urllib.urlencode({'status': msg.encode('utf-8'), 'source': self.source})
		print data
		
		fp = urllib2.urlopen(url, data)
		response = json.load(fp)
		fp.close()
		
		return response['id']

	server = "identi.ca/api"
	source = "Mu-Feeder"
