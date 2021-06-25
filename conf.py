#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import multiprocessing

bind = '0.0.0.0:9898'
workers = 20
backlog = 2048
worker_class = "gevent"
debug = False
daemon = True
proc_name = 'gunicorn1.pid'
pidfile = 'log.log'
errorlog = 'error2.log'
accesslog = 'aa.log'
loglevel = 'error'
timeout = 30
