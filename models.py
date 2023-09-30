from sklearn.linear_model import LogisticRegression
from sklearn import svm

log_reg = LogisticRegression(max_iter=1000, multi_class='ovr')
svclf = svm.SVC(kernel="rbf", C=2.3)
