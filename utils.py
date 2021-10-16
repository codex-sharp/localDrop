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


def generate_share_link(file, IP_ADDRESS):
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
    share_link = 'http://' + IP_ADDRESS + '?fid=' + str(fid)
    print('File share link:\n {}'.format(share_link))


def delete_shared_file(fpath):
    sql = """DELETE FROM `files` WHERE fpath = '{}'""".format(fpath)
    cur.execute(sql)
    con.commit()

    
def get_file_path(url):
    # extract fid from the url
    qs_dict = parse_qs(urlparse(url)[4])
    fid = qs_dict['fid']
    sql = """SELECT * FROM `files` WHERE fid = '{}'""".format(fid[0])
    cur.execute(sql)
    res = cur.fetchone()
    if res == None:
        raise ValueError("Invalid url")
    print(res['fpath'])
    return res['fpath']


def list_files_shared():
    sql = """SELECT * FROM `files`"""   
    cur.execute(sql)
    files = cur.fetchall()
    for file in files:
        print('File id: {}, File path: {}'.format(file['fid'], file['fpath']))
