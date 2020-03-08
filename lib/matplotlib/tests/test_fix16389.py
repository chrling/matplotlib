import matplotlib.text as txt
import matplotlib.pyplot as plt
import numpy as np


def test_kwargs_order():
    #General case
    a = txt.Text(size=20, fontproperties="SimHei") 
    assert a.get_size() == 20
    
    #Case from bug report
    data = np.random.randn(10000)
    plt.hist(data, bins=40, facecolor="blue", edgecolor="black", alpha=0.5)
    fp_first = plt.xlabel("value", fontproperties='SimHei',size=20)
    size_first = plt.ylabel("counts",size=20, fontproperties='SimHei')
    assert fp_first.get_size() == 20
    assert size_first.get_size() == 20