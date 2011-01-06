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

# the account type to post to, current possible vaules are: 'identica', 
# 'twitter' or 'statusnet'
ACCOUNT_TYPE		= "statusnet"

# login name and password for the account specified above
ACCOUNT_LOGIN 		= "custommade"
ACCOUNT_PASSWORD 	= "root"

# for StatusNet accounts the hostname and path of the API must be provided
# don't add a 'http://'!!!!
STATUSNET_SERVER	= "stats.custommade.com/statusnet/api"

# the URL shortener to use, currently the only supported option is 'trim'
URL_SHORTENING_SERVICE 	= "trim"

# optional username and password for the URL shortener, usually used to
# enable ownership and tracking of shortened URLs.
URL_SHORTENER_LOGIN 	= ""
URL_SHORTENER_PASSWORD 	= ""

# full URL of the feed to parse
#FEED_URL = "http://example.com/myfeed.xml"

# short prefix to add to posted messages
#POST_PREFIX = "New Blog Post: "

# maximum number of new items to post
#MAX_ITEMS = 5

# the filename where Mu-Feeder will keep its database of posted items
#DATABASE_FILE = "mu-feeder.db"
