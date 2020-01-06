class SpiralArray:
    def __init__(self, row, col):
        self.maxcol = col-1
        self.maxrow = row-1
        self.factors={
            "right":(0,1),
            "down":(1,0),
            "left":(0,-1),
            "up":(-1,0)
        }
        self.init()

    def init(self):
        self.cur=0
        self.curPoint=0,0
        self.map()={}
        for r in range(self.maxrow):
            for c in range(self.maxcol+1):
                self.map[r,c] = -1
        self.map[self.curPoint]
