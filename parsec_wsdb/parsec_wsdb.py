from wsdb_query import run_query

_ISOCHRONE_TABLE = "isochrones.girardi_ugrizzyjhk"

_iso_index = None

class IsochroneIndex(object):
    def __init__(self):
        self._build_index()

    def _build_index(self):
        query = """
            SELECT DISTINCT isoid, feh, logage
            FROM {table}
        """.format(table = _ISOCHRONE_TABLE)

        tab = run_query(query)

        self.index = {
            'feh' : tab['feh'].data,
            'logage' : tab['logage'].data,
            'isoid' : tab['isoid'].data
        }

    def _get_closest(self, colname, value):
        idx = abs(self.index[colname] - value).argmin()
        return self.index[colname][idx]

    def get_isoid(self, feh, logage):
        feh_closest = self._get_closest('feh', feh)
        logage_closest = self._get_closest('logage', logage)

        return self.index['isoid'][(self.index['feh'] == feh_closest) &
                                   (self.index['logage'] == logage_closest)][0]


class ParsecIsochrones(object):
    def __init__(self):
        global _iso_index
        if _iso_index is None or not isinstance(_iso_index, IsochroneIndex):
            _iso_index = IsochroneIndex()
        self.index = _iso_index
        self.cache = {}

    def get_isochrone(self, feh, logage, nocache=False):
        isoid = self.index.get_isoid(feh, logage)

        if nocache:
            return self._get_isochrone_from_wsdb(isoid)

        if isoid in self.cache:
            return self.cache[isoid]
        else:
            tab = self._get_isochrone_from_wsdb(isoid)
            self.cache[isoid] = tab
            return tab


    def _get_isochrone_from_wsdb(self, isoid):
        """ Grab a specific isochrone from wsdb """

        query = """
            SELECT *
            FROM {table}
            WHERE isoid = {isoid}
        """.format(table = _ISOCHRONE_TABLE, isoid = isoid)

        return run_query(query)
