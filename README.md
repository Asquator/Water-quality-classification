# Water-quality-classification

Classification algorithms comparison on water quality classification problem
Algorithms (ranked best to worst):
1. SVM Gaussian
2. SVM polynomial
3. Logistic regression
4. Naive Bayes

- Also added GDA algorithms for comparison -

Possible training output:

Algorithm: logistic
              precision    recall  f1-score   support

           0       0.93      0.97      0.95       855
           1       0.61      0.36      0.46       105
    accuracy                           0.91       960
    macro avg      0.77      0.67      0.70       960
    weighted avg   0.89      0.91      0.89       960

[[831  24]
 [ 67  38]]
Training accuracy = 0.9074758385446277
Test accuracy = 0.9052083333333333
Algorithm: SVM Gaussian
              precision    recall  f1-score   support

           0       0.96      0.99      0.98       855
           1       0.91      0.68      0.78       105
    accuracy                           0.96       960
    macro avg       0.94      0.83      0.88       960
    weighted avg       0.96      0.96      0.95       960

[[848   7]
 [ 34  71]]
Training accuracy = 0.9658897100625355
Test accuracy = 0.9572916666666667
Algorithm: SVM polynomial
              precision    recall  f1-score   support

           0       0.92      0.99      0.96       855
           1       0.86      0.34      0.49       105
    accuracy                           0.92       960
    macro avg      0.89      0.67      0.72       960
    weighted avg   0.92      0.92      0.91       960

[[849   6]
 [ 69  36]]
Training accuracy = 0.9455656623081297
Test accuracy = 0.921875
Algorithm: naive Bayes
              precision    recall  f1-score   support

           0       0.95      0.87      0.91       855
           1       0.37      0.61      0.46       105
    accuracy                           0.84       960
    macro avg      0.66      0.74      0.69       960
    weighted avg   0.88      0.84      0.86       960

[[747 108]
 [ 41  64]]
Training accuracy = 0.8460773166571915
Test accuracy = 0.8447916666666667
