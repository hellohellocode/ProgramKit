#!/usr/bin/env python3

import pytest
from database import mysql

def test_conn():
    ret = mysql.query('select 2 as num');
    assert not None is ret
    assert len(ret) == 1
    assert ret[0].get('num') == 2
