#positional arguments

def func1(a,b):
    c=a+b
    return c

out = func1(b=3,a=2)
print(out)


#default arguments

def roi(p,t,r=10):
    s_i=(p*t*r)/100
    return s_i

out = roi(10000,5,8)
print(out)


#keyword only arguments

def random_forest(n_estimators=100, *, criterion='gini', max_depth=None, min_samples_split=2, \
                  min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='sqrt', max_leaf_nodes=None, \
                  min_impurity_decrease=0.0, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, \
                  warm_start=False, class_weight=None, ccp_alpha=0.0, max_samples=None, monotonic_cst=None):
    pass


random_forest(n_estimators=200,min_samples_split=5,criterion="entorpy",bootstrap=False,class_weight=2.3,min_impurity_decrease=0.1)




#*args-variable length positional arguments

def total(*args):
    out=0
    for i in args[0]:
        out=out+i
    return out

out = total([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,56])
print(out)

#**kwargs-variable length keyword arguments

def total_kw(**kwargs):
    out=0
    for val in kwargs.values():
        out=out+val
    return out

out = total_kw(a=1,b=2,c=3,d=4,e=5)
print(out)



def demo(a, b=10, *args, c=20, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("kwargs:", kwargs)



demo(1, 2, 3, 4, c=50, d=60, e=70)




def demo1(a=5,b):
    print(a,b)

demo1(2,3)