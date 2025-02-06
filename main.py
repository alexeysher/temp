# from pathlib import Path
# from keras import models
import streamlit as st
from st_files_connection import FilesConnection

conn = st.connection('gcs', type=FilesConnection)
path = "model.h5"
# models.load_model(filepath=path, compile=False)
