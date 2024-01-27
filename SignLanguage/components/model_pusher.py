from SignLanguage.logger import logging
from SignLanguage.exception import SignException
import os,sys
from SignLanguage.entity.artifact_entity import (ModelPusherArtifact,
                                                 ModelTrainerArtifact)
from SignLanguage.entity.config_entity import ModelPusherConfig
from SignLanguage.configuration.s3_operations import s3Operation




class ModelPusher:
    def __init__(self,model_pusher_config:ModelPusherConfig,
                 model_trainer_artifact:ModelTrainerArtifact,
                 s3:s3Operation):
        self.model_pusher_config=model_pusher_config
        self.model_trainer_artifact=model_trainer_artifact
        self.s3=s3

    
    def initiate_model_pusher(self)->ModelPusherArtifact:
        try:
            logging.info(f"Entered Model Pusher initiation in ModelPusher Class")
            logging.info(f"Uploading best model to s3 bucket")
            self.s3.upload_file(
                self.model_trainer_artifact.trained_model_file_path,
                self.model_pusher_config.s3_MODEL_PATH_KEY,
                self.model_pusher_config.BUCKET_NAME,
                remove=False
            )

            model_pusher_artifact=ModelPusherArtifact(
                bucket_name=self.model_pusher_config.BUCKET_NAME,
                s3_model_path=self.model_pusher_config.s3_MODEL_PATH_KEY

            )

            logging.info(f"Exited Model Pusher initiation in ModelPusher Class")
            logging.info(f"model_pusher_artifact: {model_pusher_artifact}")
            
            return model_pusher_artifact
        

        except Exception as e:
            raise SignException(e,sys)