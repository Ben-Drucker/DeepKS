from typing import Callable, Union

def RAISE_ASSERTION_ERROR(x):
    raise AssertionError(x)

def myfunc():
    print("Hello World")

grp = "TK"

gia: dict[str, dict[str, Union[float,type]]] = {"TK": {"loss_fn": int}, "TKL": {"loss_fn": 123.456}}

loss_fn = [int(gia[grp]["loss_fn"]) for _ in range(10) if isinstance(gia[grp]["loss_fn"], int)]
