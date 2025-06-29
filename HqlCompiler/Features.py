class FeatureSet():
    def __init__(self) -> None:
        ...

class Feature():
    def __init__(self) -> None:
        ...

class Function(Feature):
    def __init__(self) -> None:
        Feature.__init__(self)
