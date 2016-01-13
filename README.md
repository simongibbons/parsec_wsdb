# parsec_wsdb

This is a simple class used to query the parsec isochrones that are stored
within wsdb, and cache them so they can be used quickly.

## Database Credentials

This package gets it's data from [wsdb](https://www.ast.cam.ac.uk/ioa/wikis/WSDB)
and as such it will need your database credentials. It will look for them in
a configuration file `.wsdb_config` which should be located in your home
directory.

The structure of the file should be

```
[wsdb]
name: wsdb
host: cappc127.ast.cam.ac.uk
user: {your username}
password: {your password}
```

Once you've created it don't forget to set it's permissions to 600!

## Usage

Once installed grabbing you can get the isochrone which is closest to a given metallicity and  age  by doing

```
import parsec_wsdb

isodb = parsec_wsdb.ParsecIsochrones()

isochrone = isodb.get_isochrone(feh = -1.5, logage =  9.0)
```

this will return an `astropy` table with the requested data.
