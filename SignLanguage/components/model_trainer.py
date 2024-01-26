from SignLanguage.logger import logging
from SignLanguage.exception import SignException
from SignLanguage.entity.config_entity import ModelTrainerConfig
from SignLanguage.entity.artifact_entity import ModelTrainerArtifact
import yaml
from SignLanguage.utils.main_utils import read_yaml_file
import os,sys




class ModelTrainer:
    def __init__(self,model_Trainer_config:ModelTrainerConfig):
        self.model_Trainer_config=model_Trainer_config


    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            logging.info(f"Entered model trainer initiation in ModelTrainer")
            logging.info(f"Unzip data")
            os.system("unzip Data.zip")
            os.system("rm Data.zip")

            with open("data.yaml",'r') as stream:
                num_classes=str(yaml.safe_load(stream)['nc'])

            model_config_file_name=self.model_Trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config=read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")
            logging.info(f"congig:{config}, {config['nc']}")
            config['nc']=int(num_classes)

            with open(f"yolov5/models/custom_{model_config_file_name}.yaml",'w') as f:
                yaml.dump(config,f)
            
            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_Trainer_config.batch_size} --epochs {self.model_Trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_Trainer_config.weight_name} --name yolov5s_results  --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            os.makedirs(self.model_Trainer_config.model_trainer_dir,exist_ok=True)
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_Trainer_config.model_trainer_dir}/")

            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")

            model_Trainer_artifact=ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt"
            )

            logging.info(f"Exited model trainer initiation in ModelTrainer")
            logging.info(f"Model Trainer artifact: {model_Trainer_artifact}")
            return model_Trainer_artifact
        
        except Exception as e:
            raise SignException(e,sys)

