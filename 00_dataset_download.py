
import os
from kaggle.api.kaggle_api_extended import KaggleApi

from utils.constants import original_dataset_folder

api = KaggleApi()
api.authenticate()

os.makedirs(original_dataset_folder, exist_ok=True)

api.dataset_download_files('olistbr/brazilian-ecommerce', path=original_dataset_folder, unzip=True)