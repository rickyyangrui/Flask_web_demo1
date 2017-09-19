#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/db_demo8'
SQLALCHEMY_TRACK_MODIFICATIONS = True


