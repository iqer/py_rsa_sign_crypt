"""
支持Python3的mysqlclient,继承自Python2的MySQLdb
用C实现,性能比pymysql好
"""
import MySQLdb
import MySQLdb.cursors as cors

# 打开数据库连接
db = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="test",
    charset='utf8',
    port=3306,
    cursorclass=cors.DictCursor
)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# sql = 'select * from EMPLOYEE'
# cursor.execute(sql)
# db.commit()
# cursor.fetchall()

sql = """insert into EMPLOYEE (`first_name`, `last_name`, `age`, `sex`, `salary`) 
values(%s,%s,%s,%s,%s)"""
try:
    cursor.executemany(sql, [('Smith', 'Tom', 15, 'M', 1500), ('Mac', 'Mohan', 20, 'M', 2000)])
    db.commit()
except Exception as e:
    # Rollback in case there is any error
    db.rollback()

# 关闭数据库
db.close()
