from pathlib import Path
from keras import models
from st_files_connection import FilesConnection

conn = st.connection('gcs', type=FilesConnection)
path = "model.h5"
# models.load_model(filepath=path, compile=False)
