# coding: utf-8
from __future__ import unicode_literals, print_function
import os
from nhentai.utils import urlparse

BASE_URL = os.getenv('NHENTAI', 'https://nhentai.net')

DETAIL_URL = '%s/api/gallery' % BASE_URL
SEARCH_URL = '%s/api/galleries/search' % BASE_URL
TAG_URL = '%s/tag' % BASE_URL
TAG_API_URL = '%s/api/galleries/tagged' % BASE_URL
LOGIN_URL = '%s/login/' % BASE_URL
FAV_URL = '%s/favorites/' % BASE_URL

u = urlparse(BASE_URL)
IMAGE_URL = '%s://i.%s/galleries' % (u.scheme, u.hostname)

PROXY = {}
