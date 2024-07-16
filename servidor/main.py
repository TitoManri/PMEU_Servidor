import oracledb

cnx = oracledb.connect(
    user= "ADMIN_MENTORIAS",
    password= "gnmap456987",
    dsn = "localhost:1521/orcl"

)

cursor = cnx.cursor()
