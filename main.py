import gdown

from pathlib import Path

print(Path('.').absolute())

url = "https://drive.google.com/file/d/1FK9WQ8ybhP1sohyB4sg9tBo4rT9xi3mv/view?usp=sharing"
path = "/mount/src/temp/model.zip"
gdown.cached_download(url, path=path, fuzzy=True)
