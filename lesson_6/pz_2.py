class Road:
    _length = 5000
    _width = 20

    def __init__(self, road_w, road_th):
        self.road_w = road_w
        self.road_th = road_th

    def road_calc(self):
        return Road._length * Road._width * self.road_w * self.road_th


a = Road(25, 5)
print(f'Масса {a.road_calc() / 1000} т.')
