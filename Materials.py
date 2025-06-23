from Colors import *


class Material:
    def __init__(self, Name: str, Color: tuple, Weight: int, fall: bool):
        self.Type = Name
        self.Color = Color
        self.Weight = Weight
        self.Fall = fall


Materials = []


def AddMaterial2List(function):
    Materials.append(function)
