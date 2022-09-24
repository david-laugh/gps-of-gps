from datetime import date


class Raw:
    def __init__(self, line) -> None:
        self._line = line
        self._values = self._extract_data()

    def _extract_data(self) -> list:
        return self._line.split(",")

    @property
    def id(self) -> str:
        return self._values[0]

    @property
    def user_id_str(self) -> str:
        return self._values[1]

    @property
    def user_lang(self) -> date:
        return self._values[2]

    @property
    def lat(self) -> float:
        return float(self._values[3])

    @property
    def lon(self) -> float:
        return float(self._values[4])

    @property
    def place_flag(self) -> str:
        return self._values[5]

    @property
    def country_code(self) -> str:
        return self._values[6]

    @property
    def cdate(self) -> str:
        return self._values[7]

    @property
    def device(self) -> str:
        return self._values[8].replace('\n','')
