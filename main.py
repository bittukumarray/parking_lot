import heapq

class ParkingLot:
  lots =[] #lots stores the parked car's and derver's details
  lot_size=0
  free_slots=[] #min heap, it tracks the minimum distacnce slot from entry
  parkedCars={} #parkedCars dictionary stores car's slot against registration_number so that searching will be in constant time agaist reistration_number
  parkedCarsByDriverAge={} #parkedCarsByDriverAge dictionary stores car's slot and reistration_number against driver's age so that searching will be in constant time agaist driver's age



  def __init__(self, lot_size):
    self.lot_size=lot_size
    self.lots=[0]*lot_size

    heapq.heapify(self.free_slots)
    for index in range(1,lot_size+1):
      heapq.heappush(self.free_slots, index)

    print("Created parking of "+str(lot_size)+" slots")


  # parkCar parks a car with given registration_number and driver_age
  def parkCar(self,registration_number, driver_age):
    if driver_age<18:
      print("driver should be on or above 18 years old")
    else:
      if len(self.free_slots)==0:
        print("no slots available")
      else:
        slot_position = self.free_slots[0]-1
        
        self.parkedCars[registration_number]={"slot":slot_position+1}

        try:
            self.parkedCarsByDriverAge[driver_age].append({"slot":slot_position+1, "registration_number":registration_number})
        except:
          self.parkedCarsByDriverAge[driver_age]=[{"slot":slot_position+1, "registration_number":registration_number}]
          
        self.lots[slot_position]={"registration_number":registration_number, "driver_age":driver_age}
        heapq.heappop(self.free_slots)
        print("Car with vehicle registration number \""+registration_number+"\" has been parked at slot number "+str(slot_position+1))


  #getSlotByRegistrationNumber searches slots of car by the given registration_number
  def getSlotByRegistrationNumber(self, registration_number):
    try:
      print(self.parkedCars[registration_number]["slot"])
    except:
        print()




  #getSlotByDriverAge searches slots of cars by the given driver's age
  def getSlotByDriverAge(self, driver_age):
    try:
      ans=""
      for slot in self.parkedCarsByDriverAge[driver_age]:
        ans= ans + str(slot["slot"])+","
      print(ans[:len(ans)-1])  
    except:
      print()

  #getRegistrationsByAge searches registration_number of cars the given driver_age
  def getRegistrationsByAge(self, driver_age):
    try:
      ans=""
      for slot in self.parkedCarsByDriverAge[driver_age]:
        ans = ans + slot["registration_number"]+","
      print(ans[:len(ans)-1])
    except:
      print()


  #vacateSlot vacates a slot with the given slot number
  def vacateSlot(self, slot_number):
    if slot_number<=self.lot_size and slot_number>0:
      if self.lots[slot_number-1]==0:
        print("No car parked at slot number "+str(slot_number))
      else:
        heapq.heappush(self.free_slots, slot_number)
        print("Slot number "+str(slot_number)+ " vacated, the car with vehicle registartion number \""+self.lots[slot_number-1]["registration_number"]+"\" left the space, the driver of the car was of age "+ str(self.lots[slot_number-1]["driver_age"]))
        self.lots[slot_number-1]=0
    else:
      print("Slot number "+ str(slot_number)+ " does not exist")    



f = open("input.txt", "r")

obj=None

for data in f:
  list_item = data.split()
  if list_item[0]=="Create_parking_lot":
    obj=ParkingLot(int(list_item[1]))
  elif list_item[0]=="Park":
    obj.parkCar(list_item[1], int(list_item[3]))
  elif list_item[0]=="Slot_numbers_for_driver_of_age":
    obj.getSlotByDriverAge(int(list_item[1]))
  elif list_item[0]=="Slot_number_for_car_with_number":
    obj.getSlotByRegistrationNumber(list_item[1])
  elif list_item[0]=="Leave":
    obj.vacateSlot(int(list_item[1])) 
  elif list_item[0]=="Vehicle_registration_number_for_driver_of_age":
    obj.getRegistrationsByAge(int(list_item[1])) 
  else:
    print("wrong query format: ", data)  

