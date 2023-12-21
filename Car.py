class Car:
    
    def __init__(self, brand,mileage, color,isAutomatic,):
        self.brand= brand
        self.mileage = mileage
        self.color =color
        self.isAutomatic = isAutomatic
        self.isManual=False
        if self.isAutomatic==False:
           self.isManual=True
    

    def show_features(self):
    
        print(self.brand,end="  ")
        print(self.mileage,end="  ")
        print(self.color,end="  ")
        if self.isAutomatic:
            print("Automatic")
        elif self.isManual:
            print("Manual")



car1 = Car("BMW",15,"Black",True)
car2=Car("Mahindra",25,"Red",False)

car1.show_features()
car2.show_features()