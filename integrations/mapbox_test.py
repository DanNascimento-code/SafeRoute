
from mapbox import get_routes

routes = get_routes("A", "B")

for r in routes:
    for key, value in r.items():
        print(f"{key}: {value}")
    print()    



