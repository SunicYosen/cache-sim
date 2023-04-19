import os

class Cache:
    def __init__(self, ways, sets, mshrs, mainpipe, loadpipes) -> None:
        self.ways      =  ways
        self.sets      =  sets
        self.mshrs     =  mshrs
        self.mainpipe  =  mainpipe
        self.loadpipes =  loadpipes