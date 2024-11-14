import os
import sys
import time
import urllib.request

import flickrapi

PER_PAGE = 400

animal_name = sys.argv[1]
api = flickrapi.FlickrAPI(
    os.environ["FLICKR_KEY"], os.environ["FLICKR_SECRET"], format="parsed-json"
)
result = api.photos.search(
    text=animal_name,
    per_page=PER_PAGE,
    media="photos",
    sort="relevance",
    safe_search=True,
    extras="url_q, license",
)
photos = result["photos"]

for i, photo in enumerate(photos["photo"]):
    url_q = photo["url_q"]
    file_path = f"./{animal_name}/{photo['id']}.jpg"
    with urllib.request.urlopen(url_q) as f:
        with open(file_path, "wb") as g:
            g.write(f.read())
    time.sleep(1)
