import gdown

url = "https://drive.google.com/file/d/1FK9WQ8ybhP1sohyB4sg9tBo4rT9xi3mv/view?usp=sharing"
gdown.cached_download(url, path='model', postprocess=gdown.extractall, fuzzy=True)
