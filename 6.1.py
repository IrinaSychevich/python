import time
class TrafficLight():
    __color = ('красный', 'желтый', 'зеленый')

    def running(self):
        print(TrafficLight.__color[0])
        time.sleep(7)
        print(TrafficLight.__color[1])
        time.sleep(2)
        print(TrafficLight.__color[2])
        time.sleep(7)

a = TrafficLight()
a.running()
