from SignLanguage.logger import logging
from SignLanguage.exception import SignException
import os, sys
from SignLanguage.entity.config_entity import (DataIngestionConfig,
                                               DataValidationConfig)
from SignLanguage.entity.artifact_entity import (DataIngestionArtifact,
                                                 DataValidationArtifact)
from SignLanguage.components.data_ingestion import DataIngestion
from SignLanguage.components.data_validation import DataValidation


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config=DataValidationConfig()

    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info(f"{'*_|-|_*' * 5} DATA INGESTION {'*_|-|_*' * 5}" )
            logging.info(f"Entered Data Ingestion phase in Training pipeline")
            logging.info(f"Getting data from url")
            
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )

            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"data extracted from url")
            logging.info(f"Exited Data Ingestion phase in Training pipeline")

            return data_ingestion_artifact
        except Exception as e:
            raise SignException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            logging.info(f"{'*_|-|_*' * 5} DATA VALIDATION {'*_|-|_*' * 5}" )
            logging.info(f"Entered Data validation phase in Training pipeline")

            data_validation = DataValidation(
                data_ingestion_artifact= data_ingestion_artifact,
                data_validation_config= self.data_validation_config
            )

            data_validation_artifact=data_validation.initiate_data_validation()
            logging.info(f"Performed data validation")
            logging.info(f"Exited Data validation phase in Training pipeline")

            return data_validation_artifact
        except Exception as e:
            raise SignException(e,sys)

        
    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)


        except Exception as e:
            raise SignException(e,sys)