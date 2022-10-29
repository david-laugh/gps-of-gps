from jsonschema import validate
import jsonschema


schema = {
    "type": "object",
    "properties": {
        "id_str": {"type": "number"},
        "user_id_str": {"type": "number"},
        "user_lang": {
            "type": "string",
            "minLength": 2,
            "maxLength": 7
        },
        "lat": {"type": "number"},
        "lon": {"type": "number"},
        "country_code": {"type": "string"},
        "cdate": {
            "type": "string",
            "format": "date"
        },
        "device": {"type": "string"},
        "category name": {"type": "string"},
        "Timezone offset in minutes": {"type": "number"},
    },
    "required": ["id_str", "user_id_str", "lat", "lon", "country_code", "cdate"],
}

data1 = {
    "id_str": "517411198141468672",
    "user_id_str": "573884537",
    "user_lang": "pl",
    "lat": 52.320863,
    "lon": 20.942055,
    "country_code": "PL",
    "cdate": "2014-10-01 20:30:17",
    "device": "Twitter for Android"
}

data2 = {
    "id_str": "517411198141468672",
    "user_id_str": "573884537",
    "user_lang": "pl",
    "lat": 52.320863,
    "lon": 20.942055,
    "country_code": "PL",
    "cdate": "abc",
    "device": "Twitter for Android"
}


def gog_validation(data):
    try:
        validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        return False


if __name__=="__main__":
    gog_validation(data1)
