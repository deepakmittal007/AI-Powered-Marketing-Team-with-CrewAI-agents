import os
import pandas as pd
import datarobot as dr
from datarobot_predict.deployment import predict
from dotenv import load_dotenv
load_dotenv(dotenv_path='/home/notebooks/storage/.env')

dr.Client()  
DEPLOYMENT_ID = os.getenv("Sales_Prediction_DEPLOYMENT_ID")

def get_sales_estimation(payload: pd.DataFrame) -> pd.DataFrame:
    predictions_df, _ = predict(
        deployment=dr.Deployment.get(DEPLOYMENT_ID),
        data_frame=payload
    )
    payload["Sales_Revenue_PREDICTION"] = predictions_df["Sales_Revenue_PREDICTION"]
    return payload