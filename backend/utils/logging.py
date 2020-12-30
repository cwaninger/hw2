"""
This module handles Logging of the App as a whole.
"""
from logging import getLogger, getLevelName, Formatter
from logging.handlers import RotatingFileHandler
from os import environ

# This class is used to dispatch different formats for different loggers
class DispatchingFormatter:
    """ DispatchingFormatter is used for Formatting Python loggers

        In Order to have different Formatting for different types of Logging
        we use this class, to be able to dispatch the formatters for loggers

        This class should not be touched.
    """

    def __init__(self, formatters, default_formatter):
        self._formatters = formatters
        self._default_formatter = default_formatter

    def format(self, record):
        formatter = self._formatters.get(record.name, self._default_formatter)
        return formatter.format(record)


def initLogging():
    """ Used to initialize our python loggers

        After receiving some basic environment Vars required, we define all 
        loggers Each Logger is defined by its logger name and the level. The 
        loggers are being initialized, and configured with name, loglevel, 
        filehandler and formatters
    """
  
    # default loglevel from environment variables by String
    log_level = getLevelName(environ.get('FLASK_LOGLEVEL'))
    sqlalchemy_log_level = environ.get('SQLALCHEMY_LOGLEVEL')
    log_folder = environ.get('FLASK_LOGFOLDER')

    # If log_level is not used and the logging levels are used directly
    # the default loglevel defined in environment is overwritten
    from logging import ERROR
    loggers = [
        {"logger": getLogger('werkzeug'), "level": log_level},              # Flask App log (restapi log)
        {"logger": getLogger('filelogger'), "level": log_level},            # Logger used for manual logging
        {"logger": getLogger('applogger'), "level": log_level},             # Logger used for manual logging
        {"logger": getLogger('sqlalchemy'), "level": sqlalchemy_log_level}, # Used for SQLALchemy (DB) Log
    ]

    # Defines rotating file handler for default log. More handlers might
    # be defined here.
    handler = RotatingFileHandler("{}/flask.log".format(log_folder), maxBytes=5000000, backupCount=10)
    handler.setFormatter(DispatchingFormatter({
            'filelogger': Formatter('[%(asctime)s]: %(name)s - {%(pathname)s:%(funcName)s:%(lineno)d} %(levelname)s - %(message)s'),
            'werkzeug': Formatter('[%(asctime)s]: %(name)s - %(levelname)s - %(message)s'),
            'applogger': Formatter('[%(asctime)s]: %(name)s - %(levelname)s - %(message)s'),
        },
        # Default if nothing specified - should not be the case 
        Formatter('%(message)s'),
    ))

    # Add Filehandler to all Loggers defined
    # Add level to all Loggers defined
    for x in loggers:
        x['logger'].addHandler(handler)
        x['logger'].setLevel(x['level'])

""" Logger definitions App usage

    If there has to be any output in the log, we have two logger defined
    which can be used. One is the filelogger which is printing additional
    output like file, function and line of log. The applogger is a simple
    log which prints just level and message.

    Warning: This behaviour can change upon configuration above!!
"""

filelogger = getLogger('filelogger')
logger = getLogger('applogger')