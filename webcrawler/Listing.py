class Listing:
    def __init__(self, objectId, finalPrice, adress, municipal, areaName, dateSold, livingAreaSqM, amountOfRooms,
                 monthlyFee, yearBuilt, elevator, balcony, firePlace):
        self.objectId = objectId
        self.finalPrice = finalPrice
        self.adress = adress
        self.municipal = municipal
        self.areaName = areaName
        self.dateSold = dateSold
        self.livingAreaSqM = livingAreaSqM
        self.amountOfRooms = amountOfRooms
        self.monthlyFee = monthlyFee
        self.yearBuilt = yearBuilt
        self.elevator = elevator
        self.balcony = balcony
        self.firePlace = firePlace

    def __repr__(self):
        return (f"Listing(price={self.finalPrice}, adress={self.adress}, "
                f"municipal={self.municipal}, area={self.areaName}, "
                f"dateSold={self.dateSold}, sqm={self.livingAreaSqM}, "
                f"rooms={self.amountOfRooms}, fee={self.monthlyFee}, "
                f"year={self.yearBuilt}, elevator={self.elevator}, "
                f"balcony={self.balcony}, fireplace={self.firePlace})")