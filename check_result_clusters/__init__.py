import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from package import (
    numpy as np,
    NDArray,
    silhouette_score
)

class Check_Score:
    def __init__(self, data : NDArray[np.int32], labels : NDArray[np.int32]) -> None:
        '''
        data : Là một vector chứa dữ liệu ban đầu chưa có nhãn
        lales : Là nhãn của dữ liệu sau khi sử dụng KMeans
        '''
        self.__data : NDArray[np.float32] = data
        self.__labels : NDArray[np.int32] = labels
    
    def show_score(self) -> float:
        return silhouette_score(self.__data, self.__labels)
