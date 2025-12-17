from src.utils import compute_review_length, compute_star_distribution
import pandas as pd

def test_compute_review_length():
    assert compute_review_length("hello world") == 2
    assert compute_review_length("") == 0


def test_compute_star_distribution():
    df = pd.DataFrame({"stars": [1, 2, 2, 3]})
    result = compute_star_distribution(df)
    assert result.loc[2] == 2