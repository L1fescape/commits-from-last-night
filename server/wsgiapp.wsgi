import site
#im assuming the folder for your app is in /var/www 
site.addsitedir('/var/www/akenn/commits/')

#change yourapp to the name of your main file
from app import app as application
