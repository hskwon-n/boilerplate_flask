from os import environ
from sqlalchemy import URL


class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = URL.create(
        "mysql",
        username=environ.get("MYSQL_USERNAME"),
        password=environ.get("MYSQL_PASSWORD"),
        host=environ.get("MYSQL_HOST"),
        port=int(environ.get("MYSQL_PORT", 3306)),
        database=environ.get("MYSQL_DATABASE"),
    ).render_as_string(hide_password=False)
