import gdown

gdown.cached_download(st.secrets['model']['url'], path='./model', postprocess=gdown.extractall, fuzzy=True)
