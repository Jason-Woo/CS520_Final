def cal_distance(a, b):
    dis = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            dis += abs(a[i][j] - b[i][j])
    return dis


def knn(train_a, train_b, test, k):
    """
        k-nearest neighbor algorithm

        Parameters
        ----------
        train_a: list
            all the train data of label a
        train_b: list
            all the train data of label b
        test: list
            all the test data
        k: int
            the parameter of knn

        Returns
        -------
        label: list
            the label of the test data
    """
    label = []
    for i in range(len(test)):
        dis_a = []
        for j in range(len(train_a)):
            dis_a.append(cal_distance(train_a[j], test[i]))

        dis_b = []
        for j in range(len(train_b)):
            dis_b.append(cal_distance(train_b[j], test[i]))

        dis_a.sort()
        dis_b.sort()
        score_a = 0
        score_b = 0
        for j in range(k):
            if dis_a[0] < dis_b[0]:
                score_a += 1
                dis_a.pop(0)
            else:
                score_b += 1
                dis_b.pop(0)
        if score_a > score_b:
            label.append('A')
        else:
            label.append('B')
    return label
