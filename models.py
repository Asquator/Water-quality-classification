from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

log_reg = LogisticRegression(max_iter=1000, multi_class='ovr')
svm_gaussian = svm.SVC(kernel="rbf", C=2.3)
svm_poly = svm.SVC(kernel="poly", degree=4, C=0.8)
nbg = GaussianNB()