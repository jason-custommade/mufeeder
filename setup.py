#!/usr/bin/env python
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

from distutils.core import setup

import mufeeder

setup(name='mufeeder',
	  #version=mufeeder.version,
	  url='http://launchpad.net/mu-feeder',
	  download_url='http://launchpad.net/mu-feeder/download',
	  author='Robert Connolly',
	  author_email='rob@webworxshop.com',
	  maintainer='Robert Connolly',
	  maintainer_email='rob@webworxshop.com',
	  license='GNU Affero GPL v3',
	  long_description="""
Mu-Feeder is intended to form a Free Software replacement to Twitterfeed
(twitterfeed.com), which posts items from an RSS feed to popular
microblogging services such as Twitter and Identi.ca.

Mu-Feeder will take a link to your RSS or Atom feed (or any feed which
feedparser can parse) and generate a summary including a shortened link
to post to the specified account. The program is written with modularity
in mind so that extra services and URL shorteners can be added easily.

Currently there is support for the Ident.ca, Twitter and StatusNet
compatible microblogging services as well as tr.im URL shortening
support. The code has been tested under Python 2.6, but should work on
earlier versions (the intention however is to move to 3.x as soon as
feedparser has been ported).""",
	  packages=['mufeeder', 'mufeeder.services', 'mufeeder.shorteners'],
          package_dir={'mufeeder':'mufeeder',
                       'mufeeder.services':'mufeeder/services',
                       'mufeeder.shorteners':'mufeeder/shorteners'},
	  classifiers=[]
	  )
