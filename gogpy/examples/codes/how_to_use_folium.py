import folium


def execute():
    m = folium.Map(location=[45.5236, -122.6750])
    m.save("index.html")


if __name__=="__main__":
    execute()
