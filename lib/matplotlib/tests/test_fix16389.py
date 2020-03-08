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

def test_if_not_set_back_to_default_xlabel():
    #Test that setting fontproperties doesn't change the other properties back to default
    data = np.random.randn(100)
    plt.hist(data, bins=40, facecolor="red", edgecolor="blue", alpha=0.6)
    original = plt.xlabel("value", fontproperties="Comic Sans MS", weight="bold", size=16)
    changed = plt.xlabel("value", weight="bold", size=16, fontproperties="Comic Sans MS")
    assert (original.get_size() == changed.get_size()) and (original.get_weight() == changed.get_weight()) and (original.get_family() == changed.get_family())

def test_if_not_set_back_to_default_ylabell():
    #Test that setting fontproperties doesn't change the other properties back to default
    data = np.random.randn(100)
    plt.hist(data, bins=40, facecolor="red", edgecolor="blue", alpha=0.6)
    original = plt.ylabell("value", fontproperties="Comic Sans MS", weight="bold", size=16)
    changed = plt.ylabell("value", weight="bold", size=16, fontproperties="Comic Sans MS")
    assert (original.get_size() == changed.get_size()) and (original.get_weight() == changed.get_weight()) and (original.get_family() == changed.get_family())
