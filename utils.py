import sqlite3 as lite
import uuid
from urllib.parse import urlparse, parse_qs

con = lite.connect('files.db')
con.row_factory = lite.Row
cur = con.cursor()


def create_tables():
    sql = """CREATE TABLE IF NOT EXISTS `files` (
	        `fid` VARCHAR(256) PRIMARY KEY,
	        `fpath` VARCHAR(256) NOT NULL
        )"""
    cur.execute(sql)


create_tables()


def generate_fid(file):
    # check if file already shared
    sql = """SELECT * FROM `files` WHERE fpath = '{}'""".format(file)
    cur.execute(sql)
    res = cur.fetchone()
    fid = None
    if res == None:
        # creating new entry
        fid = uuid.uuid4()
        sql = """INSERT INTO `files` (`fid`, `fpath`) VALUES('{}', '{}')""".format(fid, file)
        cur.execute(sql)
        con.commit()
    else:
        fid = res['fid']
    
    return fid


def get_file_path(url):
    # extract fid from the url
    qs_dict = parse_qs(urlparse(url)[4])
    print(qs_dict)
    fid = qs_dict['fid']
    sql = """SELECT * FROM `files` WHERE fid = '{}'""".format(fid[0])
    print(sql)
    cur.execute(sql)
    res = cur.fetchone()
    if res == None:
        raise ValueError("Invalid url")
    return res['fpath']
    