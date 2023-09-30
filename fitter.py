from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn


def fit(model, X, y, *args, **kwargs):
    return model.fit(X, y, *args, **kwargs)


def evaluate(model, X_train, y_train, X_test, y_test, verbose=True):
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    if verbose:
        cm = confusion_matrix(y_test, test_pred)
        cr = classification_report(y_test, test_pred, zero_division=0.0)

        print(cr)
        print(cm)
        print(f'Training accuracy = {(y_train == train_pred).sum() / len(y_train)}')
        print(f'Test accuracy = {(y_test == test_pred).sum() / len(y_test)}')

        sn.heatmap(cm, annot=True)
        plt.show()

    return train_pred, test_pred
