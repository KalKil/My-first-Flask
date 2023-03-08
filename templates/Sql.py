import pymysql
import pymysql.cursors


Connection = pymysql.connect(
    host = "10.100.33.30",
    user = "Kwilliams3",
    password = "223686940",
    database = "world",
    cursors =  pymysql.cursors.Ductcursor)
