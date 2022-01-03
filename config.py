# Programmer: Sina Fathi-Kazerooni
# Email: sina@sinafathi.com
# WWW: sinafathi.com

import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'searchapp'
