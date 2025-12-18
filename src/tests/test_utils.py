import pytest
from src.utils import split_text_data, build_logistic_pipeline

def test_split_text_data_basic():
    X = ["a"] * 100
    y = [0, 1] * 50

    X_tr, X_val, X_te, y_tr, y_val, y_te = split_text_data(X, y)

    assert len(X_te) == 20
    assert len(X_val) == 16
    assert len(X_tr) == 64

def test_build_logistic_pipeline_basic():
    model = build_logistic_pipeline(C=0.5, min_df=1)

    X = ["good food", "bad service"]
    y = [1, 0]

    model.fit(X, y)
    preds = model.predict(X)

    assert len(preds) == 2


def test_split_text_data_complex():
    X = ["a"] * 100
    y = [0] * 50 + [1] * 50 

    X_tr, X_val, X_te, y_tr, y_val, y_te = split_text_data(X, y)

    def proportion_positive(labels):
        return sum(labels) / len(labels)

    assert abs(proportion_positive(y_tr) - 0.5) < 0.05
    assert abs(proportion_positive(y_val) - 0.5) < 0.05
    assert abs(proportion_positive(y_te) - 0.5) < 0.05

def test_build_logistic_pipeline_complex():
    model = build_logistic_pipeline(C=1.0, min_df=1)

    X = [
        "excellent food and friendly staff",
        "terrible service and bad food"
    ]
    y = [1, 0]

    model.fit(X, y)
    proba = model.predict_proba(X)
    
    assert proba.shape == (2, 2)

    assert (proba >= 0).all()
    assert (proba <= 1).all()