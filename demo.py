from hate.logger import logging
from hate.exception import CustomException
import sys
from hate.configurations.gcloud_syncer import GCloudSync




#logging.info("welcome")

#try:
#    a=7/"0"
#except Exception as e:
#    raise CustomException(e, sys ) from e

obj= GCloudSync()
obj.sync_folder_from_gcloud("hate_speech_class" , "dataset.zip" , "download/dataset.zip")
