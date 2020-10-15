#!/usr/bin/env python3

import pymysql
from database import db

def query(sql, param = None):
    get_conn = db.get_db()
    conn = get_conn(pymysql)
    if conn:
        return db.query(conn, sql, param)
    else:
        return None
