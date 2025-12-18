from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def split_text_data(X, y, test_size=0.2, val_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train,
        y_train,
        test_size=val_size,
        stratify=y_train,
        random_state=random_state
    )

    return X_train, X_val, X_test, y_train, y_val, y_test

def build_logistic_pipeline(C=1.0, min_df=5):
    return Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            max_df=0.95,
            min_df=min_df,
            ngram_range=(1, 2)
        )),
        ("clf", LogisticRegression(
            C=C,
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        ))
    ])