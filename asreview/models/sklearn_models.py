import logging

from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC


def create_nb_model():
    """Return callable NaiveBayes model.

    Arguments
    ---------

    Returns
    -------
    callable:
        A function that return the Sklearn model when
        called.

    """

    model = MultinomialNB()
    logging.debug(model)

    return model


def create_svc_model():
    """Return callable SVM model.

    Arguments
    ---------

    Returns
    -------
    callable:
        A function that return the Sklearn model when
        called.

    """

    model = SVC(probability=True)
    logging.debug(model)

    return model