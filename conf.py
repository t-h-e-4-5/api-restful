#Importations
from app import app 
from flaskext.mysql import MySQL

mysql = MySQL() ## Crer une instanse mysql

####Les routes 
app.config['MYSQL_DATABASE_USER']= "root"
app.config['MYSQL_DATABASE_HOST']= "localhost"
app.config['MYSQL_DATABASE_PASSWORD']= ""
app.config['MYSQL_DATABASE_DB']= "restful-api"

#pranché
mysql.init_app(app)