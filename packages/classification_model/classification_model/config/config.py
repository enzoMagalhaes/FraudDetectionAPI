from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

VERSION = "0.1.0"
VERSION_PATH = ROOT_DIR/"VERSION"

DATASETS_DIR = ROOT_DIR / "datasets"

MODELS_DIR = ROOT_DIR / "trained_models"

MODEL_NAME = f"fraud_predictor_{VERSION}.pkl"


VARIABLES_TO_RENAME = {"Score_B.1":"Score_B_1"}


SELECTED_FEATURES = ['Sector_score', 'PARA_A', 'Score_A', 'Risk_A', 'PARA_B', 'Score_B',
       'Risk_B', 'TOTAL', 'numbers', 'Score_B_1', 'Risk_C', 'Money_Value',
       'Score_MV', 'Risk_D', 'District_Loss', 'PROB', 'RiSk_E', 'History',
       'Prob', 'Risk_F', 'Score', 'Inherent_Risk', 'CONTROL_RISK',
       'Detection_Risk', 'Audit_Risk','LOCATION_ID']

CATEGORICAL_FEATURE = 'LOCATION_ID'

NUMERICAL_FEATURES = ['Sector_score', 'PARA_A', 'Score_A', 'Risk_A', 'PARA_B', 'Score_B',
       'Risk_B', 'TOTAL', 'numbers', 'Score_B.1', 'Risk_C', 'Money_Value',
       'Score_MV', 'Risk_D', 'District_Loss', 'PROB', 'RiSk_E', 'History',
       'Prob', 'Risk_F', 'Score', 'Inherent_Risk', 'CONTROL_RISK',
       'Detection_Risk', 'Audit_Risk']

NA_INDEX = 642


VARIABLE_DROP_NA = 'Money_Value'

TARGET = 'Risk'