import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

# Define preprocessing for numeric columns (scale them)
numeric_features = ['credit_score', 'income', 'loan_amount', 'loan_term_months', 'interest_rate']
numeric_transformer = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', preprocessing.StandardScaler())
    ]
)

# Define preprocessing for categorical features (encode them)
categorical_features = ['employment_status', 'loan_purpose', 'credit_history']
categorical_transformer = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', preprocessing.OneHotEncoder(handle_unknown='ignore'))
    ]
)

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Load the saved model
model = tf.keras.models.load_model("loan_approval.keras")

# Input data
input_data = {
    'credit_score': [700],
    'income': [50000],
    'loan_amount': [20000],
    'loan_term_months': [36],
    'interest_rate': [0.05],
    'employment_status': ['employed'],
    'loan_purpose': ['car'],
    'credit_history': ['good']
}

# Convert input data to DataFrame
input_df = pd.DataFrame.from_dict(input_data)

# Preprocess the input data
input_data_preprocessed = preprocessor.transform(input_df)

# Predict the class probabilities
class_probabilities = model.predict(input_data_preprocessed)

# Convert the class probabilities to class labels
class_labels = np.argmax(class_probabilities, axis=1)

# Convert class labels to loan approval status
loan_approval_status = ['approved' if label == 1 else 'not approved' for label in class_labels]

print(loan_approval_status)