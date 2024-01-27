from SignLanguage.logger import logging
from SignLanguage.exception import SignException
from  SignLanguage.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
print("Model Pushed to S3 Bucket")