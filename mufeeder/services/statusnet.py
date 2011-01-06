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

import identica
import sys

try:
	from mufeeder import settings
except ImportError:
	print "ERROR: Can't import settings.py, please create this file!"
	sys.exit(1)

class Service(identica.Service):
	def __init__(self):
		try:
			self.server = settings.STATUSNET_SERVER
		except AttributeError:
			print "ERROR: Configuration perameter STATUSNET_SERVER is required to use the 'statusnet' service."
			sys.exit(1)
		super(Service, self).__init__()
