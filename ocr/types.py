import pathlib
from typing import Union
import inspect
import numpy as np

Path = Union[str, pathlib.Path]
Image = np.ndarray


def delegates(to=None, keep=False):
    """A decorator which replace `**kwargs` in signature with params from `to`

    For more detail see original article https://www.fast.ai/2019/08/06/delegation/
    """

    def _f(f):
        if to is None:
            to_f, from_f = f.__base__.__init__, f.__init__
        else:
            to_f, from_f = to, f
        sig = inspect.signature(from_f)
        sig_dict = dict(sig.parameters)
        k = sig_dict.pop("kwargs")
        s2 = {
            k: v
            for k, v in inspect.signature(to_f).parameters.items()
            if v.default != inspect.Parameter.empty and k not in sig_dict
        }
        sig_dict.update(s2)
        if keep:
            sig_dict["kwargs"] = k
        from_f.__signature__ = sig.replace(parameters=list(sig_dict.values()))
        return f

    return _f
