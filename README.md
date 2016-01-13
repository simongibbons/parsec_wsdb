# parsec_wsdb

This is a simple class used to query the parsec isochrones that are stored
within wsdb, and cache them so they can be used quickly.

## wsdb Credentials

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

## TODO

 * Impliment a way of grabbing them from the web so that this can be used
   outside of the IoA.
