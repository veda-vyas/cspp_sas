import sys

#activate_this = '/var/www/adsmodulepage/venv/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

activate_this = '/var/www/adsmodulepage/venv/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))

sys.path.append('/var/www/adsmodulepage')

from main import app as application
