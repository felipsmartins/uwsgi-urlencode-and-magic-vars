# coding=utf-8
from os import environ
from flask import Flask, jsonify

app = Flask(__name__)


# variáveis de ambiente não podem ter % seguido de numeral ou qualquer caracteres que gere uma "magic variable":
# https://uwsgi-docs.readthedocs.io/en/latest/Configuration.html#magic-variables

@app.route("/")
def hello_world():
    expected = 'ABC_%3F'
    current_str_after_uwsgi_ini_parse = environ.get('PASSWD')

    return jsonify({
        'expected_str': expected,
        'current_str_after_uwsgi_ini_parse': current_str_after_uwsgi_ini_parse,
        'assert_true': expected == current_str_after_uwsgi_ini_parse,
    })
