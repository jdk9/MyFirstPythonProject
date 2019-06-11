import pymysql

# 连接数据库
# db = pymysql.connect("地址", "账号", "密码", "数据库名")
db = pymysql.connect("118.126.66.89", "root", "jasmine", "jasmine_database")
# cursor游标
cursor = db.cursor()
# 执行sql语句

# cursor.execute('select * from usr')

# try:
#     cursor.execute('insert into usr values(4, "python")')
#     db.commit()
# except:
#     # db.rollback()
#     print('laji py')

cursor.execute('delete from usr')# where id=1')
db.commit()

# 接收单条数据
data = cursor.fetchall()

print(data)

# 关闭数据库连接
db.close()