from dataclasses import dataclass

import h3


@dataclass
class Cooked:
    lat : float
    lon : float
    count : int

    def h3(self, num):
        return h3.geo_to_h3(self.lat, self.lon, num)
