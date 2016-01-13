from ConfigParser import ConfigParser
import os

_CONFIG_PATH = os.path.join(os.path.expanduser('~'), ".wsdb_config")

if not os.path.isfile(_CONFIG_PATH):
    raise IOError("Cannot find wsdb credentials file: " + _CONFIG_PATH)

config = ConfigParser()
config.read(_CONFIG_PATH)

_DBNAME = config.get("wsdb", "name")
_DBUSER = config.get("wsdb", "user")
_DBPW = config.get("wsdb", "password")
_DBHOST = config.get("wsdb", "host")

import atpy
from astropy.table import Table

def run_query(query, cast_to_astropy=True):
    """ Runs the SQL query ``query`` on the database returning the output as an
    astropy table. """

    try:
        table = atpy.Table("postgres", type='sql', query=query, user=_DBUSER,\
                           database=_DBNAME, password=_DBPW, host=_DBHOST)
    except Exception as e:
        print "QUERY:"
        print query
        raise e
    # Cast into an astropy table as these are better than atpy (but can't do SQL)
    if cast_to_astropy:
        return Table(table[:])
    else:
        return table

