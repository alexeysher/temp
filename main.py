from pathlib import Path
import gdown
from keras import models

print(Path('.').absolute())

url = "https://drive.google.com/file/d/1e9hjmRHoFNxpdBx9uAkuW5kYMU1y7hvN/view?usp=sharing"
path = "model.h5"
gdown.download(url, path)
models.load_model(filepath=path, compile=False)
