from distutils.command.config import config
from energy_efficiency.config.configuration import *
from energy_efficiency.component.data_ingestion import DataIngestion
from energy_efficiency.component.data_validation import DataValidation
from energy_efficiency.entity.config_entity import DataValidationConfig
from energy_efficiency.entity.artifact_entity import DataIngestionArtifact
from energy_efficiency.pipeline.pipeline import Pipeline
from energy_efficiency.component.data_transformation import DataTransformation
import logging


def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        #config = Configuartion().get_model_evaluation_config()
        #print(config)
        #ingested = DataIngestion(data_ingestion_config=DataIngestionConfig)
        #ingested.download_energy_efficiency_data()
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()