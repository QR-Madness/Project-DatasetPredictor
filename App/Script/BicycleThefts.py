import os
from flask import current_app
import pandas as pd
from pandas import DataFrame


class BicycleThefts:
    filepath: str
    data: pd.DataFrame

    def __init__(self):
        self.filepath = os.path.join(
            current_app.root_path, "App", "Data", "Bicycle_Thefts_Open_Data.csv"
        )
        self.data = pd.read_csv(self.filepath)

    def get_description(self) -> DataFrame:
        return self.data.describe()

    