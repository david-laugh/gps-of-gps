from datetime import date


class Raw:
    def __init__(self, line) -> None:
        self._line = line
        self._values = self._extract_data(self)
        self.id = self._id()
        self.cdate = self._cdate()
        self.lat = self._lat()
        self.lon = self._lon()
        self.country_code = self._country_code()
        self.device = self._device()
        self.place_flag = self._place_flag()

    def _extract_data(self) -> list:
        return self._line.split(",")

    @property
    def _id(self) -> str:
        return self._values[0]

    @property
    def _cdate(self) -> date:
        return self._values[1]

    @property
    def _lat(self) -> float:
        return float(self._values[2])

    @property
    def _lon(self) -> float:
        return float(self._values[3])

    @property
    def _country_code(self) -> str:
        return self._values[4]

    @property
    def _device(self) -> str:
        return self._values[5]

    @property
    def _place_flag(self) -> str:
        return self._values[6]
