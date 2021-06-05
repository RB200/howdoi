class Car(object):
    def_init_(self,model,color,company,speedlimit):
        self.color=color
        self.company=company
        self.speedlimit=speedlimit
        self.model=model

    def start(self):
        print('Start it')
    def stop(self):
        print('Stop it')
    def accelerate(self):
        print('accelerate')
        'accelerator functionality here'
    def changeGear(self,gear_type):
        print('Gear Changed')
        'gear related functionality here'

audi=Car('a6','red','audi',80)
print(audi.start())