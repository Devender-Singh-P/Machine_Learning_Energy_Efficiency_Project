import os, sys
from distutils.sysconfig import PREFIX
import pandas as pd
from energy_efficiency.constant import *
from energy_efficiency.logger import logging
from energy_efficiency.exception import energy_efficiencyException
from energy_efficiency.util.util import load_object
import boto3
import botocore
from dotenv import load_dotenv

class energy_efficiencyData:

    def __init__(self,
           relative_compactness: float,
           surface_area: float,
           wall_area: float,
           roof_area: float,
           overall_height: float,
           orientation: int,
           glazing_area: float,
           glazing_area_distribution: int,
           cooling_load: float,
           heating_load: float = None
            ):
        try:
            self.relative_compactness = relative_compactness
            self.surface_area = surface_area
            self.wall_area = wall_area
            self.roof_area = roof_area
            self.overall_height = overall_height
            self.orientation = orientation
            self.glazing_area = glazing_area
            self.glazing_area_distribution = glazing_area_distribution
            self.cooling_load = cooling_load
            self.heating_load = heating_load
        except Exception as e:
            raise energy_efficiencyException(e, sys) from e

    def get_energy_efficiency_input_data_frame(self):

        try:
            energy_efficiency_input_dict = self.get_energy_efficiency_data_as_dict()
            return pd.DataFrame(energy_efficiency_input_dict)
        except Exception as e:
            raise energy_efficiencyException(e, sys) from e

    def get_energy_efficiency_data_as_dict(self):
        try:
            input_data = {
                "relative_compactness": [self.relative_compactness],
                "surface_area": [self.surface_area],
                "wall_area": [self.wall_area],
                "roof_area": [self.roof_area],
                "overall_height": [self.overall_height],
                "orientation": [self.orientation],
                "glazing_area": [self.glazing_area],
                "glazing_area_distribution": [self.glazing_area_distribution],
                "cooling_load": [self.roofcooling_load_area]
                }
            return input_data
        except Exception as e:
            raise energy_efficiencyException(e, sys)

class energy_efficiencyPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise energy_efficiencyException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise energy_efficiencyException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            heating_load = model.predict(X)
            return heating_load
        except Exception as e:
            raise energy_efficiencyException(e, sys) from e