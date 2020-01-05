from data import *
from knn import *
from nn import *

if __name__ == "__main__":
    solution_knn = knn(train_A, train_B, test, 5)
    solution_nn = nn(train_A, train_B, test, 5000)

    print('prediction made by knn: ', solution_knn)
    print('prediction made by nn: ', solution_nn)
