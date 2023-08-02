import pymysql
import pymysql.cursors as curs

# 打开数据库连接
db = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="test",
    charset='utf8',
    cursorclass=curs.DictCursor)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
# sql = 'select * from EMPLOYEE'

sql = """insert into EMPLOYEE (`first_name`, `last_name`, `age`, `sex`, `salary`) values(%s,%s,%s,%s,%s)"""

# cursor.execute(sql)
try:
    cursor.executemany(sql, [('demo', 't', 15, 'M', 1500), ('demo2', 'mm', 20, 'M', 2000)])
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.close()
