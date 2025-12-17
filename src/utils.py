def compute_review_length(text: str) -> int:
    """
    Compute the number of words in a review.

    Parameters
    ----------
    text : str
        Review text.

    Returns
    -------
    int
        Number of words in the review.
    """
    return len(str(text).split())


def compute_star_distribution(df):
    """
    Compute the distribution of star ratings.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing a 'stars' column.

    Returns
    -------
    pandas.Series
        Counts of star ratings sorted by rating.
    """
    return df["stars"].value_counts().sort_index()