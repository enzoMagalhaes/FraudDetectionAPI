import typing as t

from classification_model.config import config

import numpy as np
import pandas as pd
from marshmallow import fields, Schema, ValidationError


class TransactionDataSchema(Schema):
    Sector_score   =fields.Float()
    PARA_A         =fields.Float()
    Score_A        =fields.Float()
    Risk_A         =fields.Float()
    PARA_B         =fields.Float()
    Score_B        =fields.Float()
    Risk_B         =fields.Float()
    TOTAL          =fields.Float()
    numbers        =fields.Float()
    Score_B_1      =fields.Float()
    Risk_C         =fields.Float()
    Money_Value    =fields.Float()
    Score_MV       =fields.Float()
    Risk_D         =fields.Float()
    District_Loss  =fields.Integer()
    PROB           =fields.Float()
    RiSk_E         =fields.Float()
    History        =fields.Integer()
    Prob           =fields.Float()
    Risk_F         =fields.Float()
    Score          =fields.Float()
    Inherent_Risk  =fields.Float()
    CONTROL_RISK   =fields.Float()
    Detection_Risk =fields.Float()
    Audit_Risk     =fields.Float()
    LOCATION_ID    =fields.Str()



def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()
    if input_data[config.SELECTED_FEATURES].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=config.SELECTED_FEATURES
        )

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame
                    ) -> t.Tuple[pd.DataFrame, t.Optional[dict]]:

    #drop rows with na
    validated_data = drop_na_inputs(input_data=input_data)

    # set many=True to allow passing in a list
    schema = TransactionDataSchema(many=True)
    errors = None

    try:
        # replace numpy nans so that Marshmallow can validate
        schema.load(validated_data.replace({np.nan: None}).to_dict(orient="records"))
    except ValidationError as exc:
        errors = exc.messages


    return validated_data, errors
