from time import sleep

class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]


    def running(self):
        list_1 = []
        i = 0
        while i != 3:
            if i == 0:
                print(TrafficLight.__color[i])
                sleep(7)
                list_1.append(TrafficLight.__color[i])
            elif i == 1:
                print(TrafficLight.__color[i])
                sleep(2)
                list_1.append(TrafficLight.__color[i])
            elif i ==2:
                print(TrafficLight.__color[i])
                sleep(2)
                list_1.append(TrafficLight.__color[i])
            i += 1
        if list_1 != TrafficLight.__color:
            print("В программе есть нарушения")


a = TrafficLight()
a.running()