import os

class BaseConfig(object):
    SECRET_KEY = "somesecret"
    DEBUG = True
    DB_NAME = "module_page"
    DB_USER = "postgres"
    DB_PASS = "veda1997"
    DB_SERVICE = "localhost"
    DB_PORT = "5432"
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
)
