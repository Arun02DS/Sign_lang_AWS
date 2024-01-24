from SignLanguage.logger import logging
from SignLanguage.exception import SignException
import os, sys
from SignLanguage.entity.config_entity import DataIngestionConfig
from SignLanguage.entity.artifact_entity import DataIngestionArtifact
from SignLanguage.components.data_ingestion import DataIngestion


class TrainPipeline:
    def __init__(self):
        self.DataIngestionConfig = DataIngestionConfig()

    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info(f"Entered Data Ingestion phase in Training pipeline")
            logging.info(f"Getting data from url")
            
            data_ingestion = DataIngestion(
                data_ingestion_config=self.DataIngestionConfig
            )

            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"data extracted from url")
            logging.info(f"Exited Data Ingestion phase in Training pipeline")

            return data_ingestion_artifact
        except Exception as e:
            raise SignException(e,sys)
        
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise SignException(e,sys)