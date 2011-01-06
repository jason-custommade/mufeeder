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

import urllib2

try:
	import json
except ImportError:
	import simplejson as json

try:
	import settings
except ImportError:
	print "ERROR: Can't import settings.py, please create this file!"
	sys.exit(1)

class Shortener(object):
	
	sandbox = False
	
	def run(self, item):
		url = "http://api.tr.im/api/trim_url.json?url=" + item.link
		
		if(settings.URL_SHORTENER_LOGIN != '' and settings.URL_SHORTENER_PASSWORD != ''):
			url += "&username=" + settings.URL_SHORTENER_LOGIN + "&password=" + settings.URL_SHORTENER_PASSWORD
			
		if self.sandbox:
			url += "&sandbox=true"
			
		r = urllib2.urlopen(url)
		response = json.load(r)
		r.close()
		
		return response['url']
