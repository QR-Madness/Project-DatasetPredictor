import os
import pickle
from flask import current_app
import pandas as pd
from pandas import DataFrame
from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


class BicycleTheftsPredictor:
    """
    Bicycle Thefts Predictor Model
    """

    data_dir_path: str
    raw_data_filepath: str
    saved_model_filepath: str
    data: pd.DataFrame
    model_rfr: RandomForestRegressor
    X: pd.DataFrame
    y: pd.DataFrame

    def __init__(self):
        """
        Construct the bicycle theft predictor
        """
        # configure the directory for the theft predictor's data
        self.data_dir_path = os.path.join(current_app.root_path, "App", "Data")
        # raw data CSV file
        self.raw_data_filepath = os.path.join(
            self.data_dir_path, "Bicycle_Thefts_Open_Data.csv"
        )
        # pretrained model filename
        self.saved_model_filepath = os.path.join(
            self.data_dir_path, "BicycleTheftModel.pkl"
        )
        # ingest the CSV into a dataframe member
        self.data = pd.read_csv(self.raw_data_filepath)

    def __ingest_model__(self) -> bool:
        """
        Consume the model into the predictor's member
        :returns If the ingestion consumed a new file
        """
        try:
            self.model_rfr.get_params()
        except:
            with open(self.saved_model_filepath, "rb") as model_fs:
                self.model_rfr = pickle.load(model_fs)
                model_fs.close()
            # clean & configure the data for running tests
            self.data = self.data.dropna()
            scaler = StandardScaler()
            self.data[["X", "Y"]] = scaler.fit_transform(self.data[["X", "Y"]])
            selected_features = ["X", "Y"]
            self.X = self.data[selected_features]
            self.y = self.data["X"]
            # segment the data for getting the test data
            X_train, self.X_test, y_train, self.y_test = train_test_split(
                self.X, self.y, test_size=0.2, random_state=42
            )
            return True
        else:
            return False

    def ensure_model(self) -> bool:
        """
        Ensures that the predictor's model is working.
        """
        try:
            # ingestion does not re-read a file if the predictor's model is okay
            self.__ingest_model__()
            return True
        except Exception as e:
            raise Exception(
                "The saved model is not configured properly! Details: " + str(e)
            )

    def get_description(self) -> DataFrame:
        """
        Description of raw data
        """
        return self.data.describe()

    def get_model_info(self) -> DataFrame:
        """
        Returns a dataframe for the model's stats
        """
        self.ensure_model()
        y_pred_rf = self.model_rfr.predict(self.X_test)
        rfr_mse = (mean_squared_error(self.y_test, y_pred_rf),)
        rfr_regressions_r_sq = r2_score(self.y_test, y_pred_rf)
        df_data = {
            "Random Forest Regression R-squared:": [rfr_mse.__str__()],
            "MSE (Mean Squared Error)": [rfr_regressions_r_sq.__str__()],
        }
        return pd.DataFrame(df_data)

    def get_predictions(self) -> DataFrame:
        self.ensure_model()
        y_pred_rf = self.model_rfr.predict(self.X_test)
        return pd.DataFrame(y_pred_rf).describe()