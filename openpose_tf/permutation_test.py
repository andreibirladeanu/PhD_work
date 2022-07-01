from scipy import stats
def permutation_test(X,y,groups, clf):
    """function that does 100 permutations of the dataset keeping groups and labels together and returns p value"""
    _scores = []
    for i in range(0,100):
        y_shuffled,groups_shuffled= shuffle(y,groups,random_state=i)
        scoring = ['accuracy', 'recall','precision','f1']
        scaler = preprocessing.StandardScaler()
        pipe = Pipeline(steps=[("scaler", scaler), ("clf", clf)])
        cv = GroupKFold(n_splits=5)
        scores = cross_validate(pipe, X, y_shuffled,groups=groups_shuffled, cv=cv, scoring=scoring)
        _scores.append(np.mean(scores['test_accuracy']))
    score_no_perm = cross_validate(pipe, X_shuffled, y_shuffled,groups=groups_shuffled, cv=cv, scoring=scoring)
    t_test = stats.ttest_1samp(_scores, np.mean(score_no_perm['test_accuracy']))
    return(t_test.pvalue)