import collections.abc

d={'level1':{'level2':{'levelA':0,'levelB':1}}}
u={'level1':{'level2':{'levelB':10}}}


def update_dict(d, u):
    if isinstance(u, dict):
        for k, v in u.items():
            if isinstance(v, collections.abc.Mapping):
                print("this is the passed key", d.get(k, {}))
                d[k] = update_dict(d.get(k, {}), v)
                print("this is the value being passed", v)
            else:
                d[k] = v
        return d
    else:
        raise Exception("second parameter isn't a dictionary")



update_dict(d, u)
print(d)

