from sklearn.model_selection import train_test_split

from models import *
from fitter import *
from dataset import Dataset

models = {'logistic': log_reg,
          'SVM Gaussian': svm_gaussian,
          'SVM polynomial': svm_poly,
          'naive Bayes' : nbg,
          'Linear GDA' : lGDA,
          'Quadratic GDA' : qGDA}

if __name__ == '__main__':
    ds = Dataset()
    X, y = ds.X, ds.y
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.12)

    for name, model in models.items():
        print("Algorithm: " + name)
        fit(model, X_train, y_train)
        evaluate(model, X_train, y_train, X_test, y_test)
