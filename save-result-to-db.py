#! /usr/local/bin/python3
# -*- coding:utf-8 -*-

import sys
import os
import psycopg2

print("python3 连接pg数据库")
if len(sys.argv) != 4 :  print("缺少必要参数");exit();
print("脚本的路径: " + sys.argv[0])
print("参数PV: " + sys.argv[1])
print("参数UV: " + sys.argv[2])
print("参数IP: " + sys.argv[3])

db_host = os.getenv("DB_HOST")
if db_host is None: db_host = "127.0.0.1"
db_port = os.getenv("DB_PORT")
if db_port is None: db_port = "5432"
db_user = os.getenv("DB_USER")
if db_user is None: db_user = "postgres"
db_password = os.getenv("DB_PASSWORD")
if db_password is None: db_password = "postgres"
db_database = os.getenv("DB_DATABASE")
if db_database is None: db_database = "postgres"

#db_host = "192.168.4.44"
#db_port = "5432"
#db_user = "postgres"
#db_password = "postgres"
#db_database = "postgres"

conn = psycopg2.connect(database=db_database, user=db_user, password=db_password, host=db_host, port=db_port)
cur = conn.cursor()
# 执行查询命令
#cur.execute("insert into td_vist_quantity (pv,uv,ip,create_time) select 55,22,44,now();")
cur.execute("insert into td_vist_quantity (pv,uv,ip,create_time) select " + sys.argv[1] + "," + sys.argv[2] + "," + sys.argv[3]  + ",now();")
cur.execute("select * from td_vist_quantity order by id desc limit 1;")

# 获取结果集的每一行
rows = cur.fetchall()
# 获取所有字段名
all_fields = cur.description


# 首先打印字段名
field_messages = []
for i in range(len(all_fields)):
    # 格式化输出结果，len参数是各列的显示宽度，可以指定常量，也可自定义函数进行获取。
    field_messages.append("{str:<{len}}".format(str=str(all_fields[i][0]), len=50))

field_message = "".join(field_messages)
print(field_message)

# 然后逐行打印结果集
for row in rows:
    row_messages = []
    for j in range(len(row)):
        # 格式化结果集
        row_messages.append("{str:<{len}}".format(str=str(row[j]), len=50))
    row_message = "".join(row_messages)
    print(row_message)

# 获取结果集的每一行
rows = cur.fetchall()
# 获取所有字段名
all_fields = cur.description
# 写入文件results.txt中，此处需要填写实际路径名
with open("results.txt", "w", encoding="utf-8") as f:
    # 首先写入字段名
    field_messages = []
    for i in range(len(all_fields)):
        # 格式化输出结果，len参数是各列的显示宽度，可以指定常量，也可自定义函数进行获取。
        field_messages.append("{str:<{len}}".format(str=str(all_fields[i][0]), len=50))
    field_message = "".join(field_messages)
    f.write(field_message + "\n")

    # 然后写入结果集
    for row in rows:
        row_messages = []
        for j in range(len(row)):
            # 格式化结果集
            row_messages.append("{str:<{len}}".format(str=str(row[j]), len=50))
        row_message = "".join(row_messages)
        f.write(row_message + "\n")

# 有插入语句，所以需要提交事务
conn.commit()
# 关闭连接
conn.close()
