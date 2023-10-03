import configparser
import sys

config = configparser.RawConfigParser()
config.read(sys.path[0] + "/pytest.ini")


def get_browser():
    return config.get('test env', 'browser')


def get_app_url():
    return config.get('test env', 'base_url')


def get_username():
    return config.get('test env', 'username')


def get_password():
    return config.get('config data', 'password')


def get_timeperiod():
    return config.get('test env', 'time_period')



def get_polling_frequency():
    return config.get('test env', 'polling_frequency')
