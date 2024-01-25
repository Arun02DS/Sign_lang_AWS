import os
from dataclasses import dataclass
from datetime import datetime
from SignLanguage.constant.training_pipeline import *
from typing import List

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    artifacts_dir=os.path.join(ARTIFACT_DIR,TIMESTAMP)

training_pipeline_config:TrainingPipelineConfig=TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir:str = os.path.join(
        training_pipeline_config.artifacts_dir,DATA_INGESTION_DIR_NAME
    )

    feature_store_file_path:str=os.path.join(
        data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR
    )

    data_download_url:str=DATA_DOWNLOAD_URL

@dataclass
class DataValidationConfig:
    data_validation_dir:str=os.path.join(
        training_pipeline_config.artifacts_dir,DATA_VALIDATION_DIR_NAME
    )

    valid_status_file_dir:str=os.path.join(data_validation_dir,DATA_VALIDATION_STATUS_FILE)

    required_file_list:List=DATA_VALIDATION_ALLREQUIRED_FILES

