#!/usr/bin/env python3

import configparser
import abc
import os
import collections
from DBUtils.PooledDB import PooledDB
from database import const

def get_db():
    conn_pool = None

    def _get_conn(creator):
        nonlocal conn_pool
        if None is conn_pool:
            conn_pool = init_db(creator)
        return conn_pool.connection()

    return _get_conn

def init_db(creator):
    if os.path.exists(const.CONF_FILE):
        dbconf = get_conf_by_file(const.CONF_FILE)
    else:
        dbconf = get_conf_by_env()
        if None is dbconf:
            dbconf = get_conf(creator)

    return create_conn_pool(dbconf)

def get_conf(creator, host = 'dev.mysql',
    port = 3306, name = 'db_test',
    user = 'test', passwd = 'test',
    mincached = 1, maxcached = 1,
    maxconnections = 1, maxshared = 1,
    blocking = 1, ping = 1):
    return {
            'creator' : creator,
            'host' : host,
            'port' : port,
            'name' : name,
            'user' : user,
            'passwd' : passwd,
            'mincached' : mincached,
            'maxcached' : maxcached,
            'maxconnections' : maxconnections,
            'maxshared' : maxshared,
            'blocking' : blocking,
            'ping' : ping
            }

def get_conf_by_env():
    try:
        conf_file = os.environ[const.ENV_CONF_FILE]
        return get_conf_by_file(conf_file)
    except KeyError:
        return None
    
def get_conf_by_file(conf_file):
    if None is conf_file:
        raise 

    conf = configparser.ConfigParser()
    conf.read(conf_file)
    return get_conf(
        conf.get('db', 'creator'),
        conf.get('db', 'host'),
        conf.get('db', 'port'),
        conf.get('db', 'name'),
        conf.get('db', 'user'),
        conf.get('db', 'passwd'),
        conf.get('db', 'mincached'),
        conf.get('db', 'maxcached'),
        conf.get('db', 'maxconnections'),
        conf.get('db', 'maxshared'),
        conf.get('db', 'blocking'),
        conf.get('db', 'ping')
        )

def create_conn_pool(dbconf):
    conn_pool = PooledDB(creator=dbconf['creator'],
        host=dbconf['host'],
        port=dbconf['port'],
        db=dbconf['name'],
        user=dbconf['user'],
        passwd=dbconf['passwd'],
        mincached=dbconf['mincached'],
        maxcached=dbconf['maxcached'],
        maxconnections=dbconf['maxconnections'],
        maxshared=dbconf['maxshared'],
        blocking=dbconf['blocking'],
        ping=dbconf['ping']
        )
    return conn_pool

def execute(conn, sqls, auto_commit = True, auto_close = True, hook_cur = None):
    if None is conn:
        return None

    cur = None
    try:
        cur = conn.cursor()
        ret = []
        for tp in sqls:
            if tp[1]:
                cur.execute(tp[0], tp[1])
                if hook_cur:
                    ret.append(hook_cur(cur))
            else:
                cur.execute(tp[0])
                if hook_cur:
                    ret.append(hook_cur(cur))
        if auto_commit:
            conn.commit()
        return conn, cur, ret
    except Exception as e:
        if auto_commit and conn:
            conn.rollback()
        raise Exception("Failed to execute sql: " + str(e))
    finally:
        if auto_close:
            if cur:
                cur.close()
            if auto_close and conn:
                conn.close()

def insert(conn, sqls, auto_close):
    def getlastid(cur):
        return cur.lastrowid()

    return execute(conn, sqls, hook_cur = getlastid, auto_close = auto_close)

def update(conn, sql, param, auto_close):
    sqls = [(sql, param)]
    return execute(conn, sqls, auto_close = auto_close)

def query(conn, sql, param, auto_close=True):
    def getall(cur):
        return (cur.fetchall(), cur.description)

    sqls = [(sql, param)]
    _, _, ret= execute(conn, sqls, hook_cur = getall)
    if ret:
        return convert_ret(ret[0][0], ret[0][1])
    else:
        return None

def convert_ret(res_all, description):
    rows = []
    if res_all is None:
        return rows
    for res in res_all:
        row = {}
        for i in range(len(description)):
            row[description[i][0]] = res[i]
        rows.append(row) 
    return rows
