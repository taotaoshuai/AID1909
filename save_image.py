import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")
cur = db.cursor()
# 生成游标对象（用于操作数据库数据，获取sql执行结果的对象）
with open('jize.jpg','rb') as f:
    data=f.read()
try:
    sql = "update cls1 set img=%s where id=1;"
    cur.execute(sql,[data])
    db.commit()
except Exception as e:
    print(e)



#读取文件
sql="select img from cls1 where id=1"
cur.execute(sql)
data=cur.fetchone()
print(data)
with open("tom.jpg","wb")as f:
    f.write(data[0])
cur.close()
db.close()
