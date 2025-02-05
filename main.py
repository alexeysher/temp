import gdown

from pathlib import Path

print(Path('.').absolute())

url = "https://drive.google.com/file/d/1u_5ifSE9mZiuS3364mUXl-F1tQ2xGz6G/view?usp=sharing"
path = "model.h5"
gdown.download(url, path)
