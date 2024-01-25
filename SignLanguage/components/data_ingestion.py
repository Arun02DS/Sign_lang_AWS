from SignLanguage.logger import logging
from SignLanguage.exception import SignException
from SignLanguage.entity.config_entity import DataIngestionConfig
from SignLanguage.entity.artifact_entity import DataIngestionArtifact
import os,sys
import zipfile
from six.moves import urllib



class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise SignException(e,sys)
        
    def download_data(self)->str:
        """
        Description: This function download data from url.

        Return: string of zip file path

        """
        try:
            dataset_url=self.data_ingestion_config.data_download_url
            zip_download_dir=self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir,exist_ok=True)
            data_file_name=os.path.basename(dataset_url)
            zip_file_path=os.path.join(zip_download_dir,data_file_name)
            logging.info(f"downloading data from {dataset_url} into file {zip_file_path}")
            urllib.request.urlretrieve(dataset_url,zip_file_path)
            logging.info(f"downloaded data from {dataset_url} into file {zip_file_path}")
            return zip_file_path
        
        except Exception as e:
            raise SignException(e,sys)
        
    def extract_zip_file(self,zip_file_path:str)->str:
        """
        Description: Extract zip file content.

        Return: None
        
        """

        try:
            feature_store_path=self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path,exist_ok=True)
            with zipfile.ZipFile(zip_file_path,'r') as zip_ref:
                zip_ref.extractall(feature_store_path)
            logging.info(f"Extracting zip file {zip_file_path} into dir:{feature_store_path}")

            return feature_store_path
        
        except Exception as e:
            raise SignException(e,sys)
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info(f"Data Ingestion initiated")
            zip_file_path=self.download_data()
            feature_store_path=self.extract_zip_file(zip_file_path=zip_file_path)
            
            data_ingestion_artifact=DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info(f"data ingestion exited")
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        
        except Exception as e:
            raise SignException(e,sys)