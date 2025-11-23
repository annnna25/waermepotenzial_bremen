import geopandas as gpd
import matplotlib.pyplot as plt

# Pfad zum Shapefile
shapefile_path = "bremen-heat-project/data/geoportal/data/geoportal/AX_GeoreferenzierteGebaeudeadresse.shp"

# Einlesen der Gebäudedaten als GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# Erste Zeilen anzeigen
print(gdf.head())

# Geometrien anschauen (entählt polygon daten)
print(gdf.geometry.head())

# Karte plotten der Gebäudeadressen (zeigt eindache Karte)
gdf.plot(figsize=(10,10), color='lightblue', edgecolor='black')
plt.title("Gebäudeadressen Bremen")
plt.show()