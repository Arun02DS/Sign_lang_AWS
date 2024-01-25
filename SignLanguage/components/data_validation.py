from SignLanguage.logger import logging
from SignLanguage.exception import SignException
from SignLanguage.entity.artifact_entity import (DataValidationArtifact,
                                                 DataIngestionArtifact)
from SignLanguage.entity.config_entity import DataValidationConfig
import os,sys
import shutil





class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config

        except Exception as e:
            raise SignException(e,sys)
    
    def validate_all_files(self)->bool:
        """
        Description: This function validated files in feature store.

        Return: Boolean

        """
        try:
            validation_status=None

            all_files=os.listdir(self.data_ingestion_artifact.feature_store_path)

            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status=False
                    os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status=True
                    os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir,'w') as f:
                        f.write(f"Validation status: {validation_status}")
            logging.info(f"validation status updated in directory.")
            return validation_status
        
        except Exception as e:
            raise SignException(e,sys)

    def initiate_data_validation(self)->DataIngestionArtifact:
        try:
            logging.info(f"Entered data validation initiation in Datavalidation class")
            status=self.validate_all_files()

            data_validation_artifact=DataValidationArtifact(
                validation_status=status
            )

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path,os.getcwd())

            logging.info(f"Exited data validation initiation in Datavalidation class")
            logging.info(f"data_validation_artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise SignException(e,sys)
