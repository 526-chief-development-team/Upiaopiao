import xlwt  # 进行Excel操作
import sqlite3  # 进行SQLite数据库操
from spider import askUrl,getData

def main():
    saveDapath = 'Web-chengdu'
    saveDB(saveDapath)


def init_DB(saveDBpath):
    sql = '''
     create table webchengdu(
     id integer primary key autoincrement,
     jobname varchar,
     companyhref text,
     companyname varchar,
     providesalarytext text,
     jobwelf text,
     workrequest varchar,
     workplace varchar ,
     workminimumDegree varchar,
     workrecruiternum text
        )
        '''  # 创建数据表
    conn = sqlite3.connect(saveDBpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()


def saveDB(saveDBpath):
    datalist = getData()
    init_DB(saveDBpath)
    conn = sqlite3.connect(saveDBpath)
    cur = conn.cursor()
    for item in datalist:
        sql = '''
        insert into webchengdu(
        jobname,companyhref,companyname,providesalarytext,jobwelf,workrequest,workplace,workminimumDegree,workrecruiternum)
        values("%s","%s","%s","%s","%s","%s","%s","%s","%s")''' % (item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8])
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
