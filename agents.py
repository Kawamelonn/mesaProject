import mesa
from mesa import Agent

class Street(mesa.Agent):
  def __init__(self, unique_id, model, direction = [0,0]):
    super().__init__(unique_id, model)
    self.direction = direction
  def __str__(self):
    return f"Street"
  
class Building(mesa.Agent):
  def __init__(self, unique_id, model, pos):
    super().__init__(unique_id, model)
    self.pos = pos
  def __str__(self):
    return f"Building {self.pos}"
  

class TrafficLight(mesa.Agent):
  def __init__(self, unique_id, model, pos, redLight=True, counter=1):
      super().__init__(unique_id, model)
      self.pos = pos
      self.redLight = redLight
      self.counter = counter
  def __str__(self):
      return f"Light{self.pos}"

  def step(self):
    #print(self.unique_id, " I stepped inside trafficLight!")
    if self.counter == 5:
      self.redLight = not self.redLight
      self.counter = 1
    else:
      self.counter+=1
    #print(self.unique_id, self.redLight)

class ParkingSpace(mesa.Agent):
  def __init__(self, unique_id, model, pos):
    super().__init__(unique_id, model)
    self.pos = pos
  def __str__(self):
    return f"Park {self.pos}"
  
class Car(mesa.Agent):
    def __init__(self, unique_id, model, pos, parking_space_pos, moving=True, parked=False):
        super().__init__(unique_id, model)
        self.pos = pos
        self.parking_space_pos = parking_space_pos
        self.moving = moving
        self.parked = parked

    def step(self):
      if not self.moving and not self.parked:
        current_cell = self.model.grid.get_cell_list_contents(self.pos)
        neighbors = self.grid.get_neighbors(current_cell, moore=True)
        for i in neighbors:
          print(i)
        for a in current_cell:
          if isinstance(a, TrafficLight) and not a.redLight:
            print("Moving again")
            self.moving = True
          elif isinstance(a, TrafficLight) and a.redLight:
            print("I'm stopped")
      if self.moving and not self.parked:
        x, y = self.pos
        print(self.model.schedule.steps, x, y, self.parking_space_pos)
        next_x = x + 1
        if (next_x, y) == self.parking_space_pos:
          print("I parked!")
          parked = True
          self.model.grid.move_agent(self, (next_x, y))
        if 0 <= next_x < self.model.grid.width:
            next_cell = self.model.grid.get_cell_list_contents((next_x, y))
            #print(f"Next Position: {next_cell}")
            for a in next_cell:
              if isinstance(a, Street):
                self.model.grid.move_agent(self, (next_x, y))
                print("Next square is a street")
                if isinstance(a, Building):
                    print("Next suqare is a building")
                    self.moving = False
              if isinstance(a, TrafficLight):
                print("Reached a trafficLight")
                if a.redLight:
                  print("Reached a red trafficlight")
                  self.moving = False
                else:
                  print("Reached a green trafficLight")
                  self.moving = True
        else:
          print("Next square is outside of the grid")
          self.moving = False

