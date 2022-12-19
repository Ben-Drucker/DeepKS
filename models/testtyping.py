import typing
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

class Supports(typing.Protocol):
    i: int
    def pow(self, X, y, *args) -> int:
        ...

class A:
    def __init__(self, i: int):
        self.i = i
    def pow(self, X, y, z, a, b, c, d) -> int:
        return self.i ** X

a: Supports = A(1)

@typing.runtime_checkable
class AcceptableClassifier(typing.Protocol):
    def fit(self, X, y, *args) -> typing.Any:
        ...
    def predict(self, X, *args) -> typing.Any:
        ...
    def predict_proba(self, X, *args) -> typing.Any:
        ...
    def score(self, X, y, *args) -> typing.Any:
        ...

def factory(acceptable_classifier: AcceptableClassifier) -> AcceptableClassifier:
    class NewClass(acceptable_classifier.__class__):
        def fit(self, X, y, *args) -> typing.Any:
            print("Yup. You're using the right method.")
            return super().fit(X, y)
        def predict(self, X, *args) -> typing.Any:
            return super().predict(X)
        def predict_proba(self, X, *args) -> typing.Any:
            return super().predict_proba(X)
        def score(self, X, y, *args) -> typing.Any:
            return super().score(X, y)
    
    NewClass.__name__ = acceptable_classifier.__class__.__name__ + "New"
    acceptable_classifier.__class__ = NewClass
    
    return acceptable_classifier

# class myKNeighborsClassifier(KNeighborsClassifier):
#     def fit(self, X, y, *args) -> typing.Any:
#         return super().fit(X, y)
#     def predict(self, X, *args) -> typing.Any:
#         return super().predict(X)
#     def predict_proba(self, X, *args) -> typing.Any:
#         return super().predict_proba(X)
#     def score(self, X, y, *args) -> typing.Any:
#         return super().score(X, y)

aa: AcceptableClassifier = factory(KNeighborsClassifier())
aa.fit(None, None)
bb: AcceptableClassifier = factory(RandomForestClassifier())