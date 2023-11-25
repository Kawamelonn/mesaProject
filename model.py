from ast import JoinedStr
import mesa
from mesa.space import MultiGrid
from mesa.time import RandomActivationByType
from agents import Street, Building, TrafficLight, ParkingSpace, Car

class TrafficModel(mesa.Model):
  def __init__(
      self,
      height=24,
      width=24,
      car_count = 5,
      ):
    super().__init__()
    self.height = height
    self.width = width
    self.grid = MultiGrid(width, height, torus = False)
    self.schedule = RandomActivationByType(self)

    agent_id = 0

    parking_pos = [(9, 2), (2, 3), (11, 4), (6, 5), (17, 3), (20, 4), (4, 10),
                   (8, 8), (11, 10), (16, 10), (21, 9), (2, 17), (5, 20),
                   (8, 20), (17, 17), (20, 17), (20, 20)]

    for pos in parking_pos:
      parking_agent = ParkingSpace(agent_id, self, pos)
      self.grid.place_agent(parking_agent, pos)
      self.schedule.add(parking_agent)
      agent_id += 1

    building_pos = []

    for i in range(2, 6):
      for j in range(2, 12):
        building_pos.append((j, i))
    for i in range(2, 6):
      for j in range(16, 18):
        building_pos.append((j, i))
    for i in range(2, 6):
      for j in range(20, 22):
        building_pos.append((j, i))
    for i in range(8, 12):
      for j in range(2, 5):
        building_pos.append((j, i))
    for i in range(8, 12):
      for j in range(7, 12):
        building_pos.append((j, i))
    for i in range(8, 12):
      for j in range(16, 18):
        building_pos.append((j, i))
    for i in range(8, 12):
      for j in range(20, 22):
        building_pos.append((j, i))
    for i in range(16, 22):
      for j in range(2, 6):
        building_pos.append((j, i))
    for i in range(16, 22):
      for j in range(8, 12):
        building_pos.append((j, i))
    for i in range(16, 18):
      for j in range(16, 22):
        building_pos.append((j, i))
    for i in range(20, 22):
      for j in range(16, 22):
        building_pos.append((j, i))
    for i in range(13, 15):
      for j in range(13, 15):
        building_pos.append((j, i))

    for pos in building_pos:
        if pos not in parking_pos:
            building_agent = Building(agent_id, self, pos)
            self.grid.place_agent(building_agent, pos)
            self.schedule.add(building_agent)
            agent_id += 1

        for i in range(width):
                for j in range(height):
                    if (i, j) not in building_pos and (i, j) not in parking_pos:
                        agent = Street(agent_id, self, (i,j))
                        self.grid.place_agent(agent, (i, j))
                        self.schedule.add(agent)
                        agent_id += 1

        red_light_values = [True, True, False, False, True, True, False, False,
                                False, False, True, True, False, False, True, True,
                                True, True, False, False, False, False, True, True]

        traffic_pos = [(0, 11), (1, 11), (2, 12), (2, 13), (5, 8), (6, 8), (7, 6),
        (7, 7), (11, 22), (11, 23), (14, 2), (15, 2), (16, 0), (16, 1), (12, 21),
        (13, 21), (14, 20), (15, 20), (16, 19), (16, 18), (21, 14), (21, 15),
        (22, 16), (23, 16)]

        for i, pos in enumerate(traffic_pos):
            red_light = red_light_values[i]
            traffic_agent = TrafficLight(agent_id, self, pos, red_light)
            self.grid.place_agent(traffic_agent, pos)
            self.schedule.add(traffic_agent)
            #print(traffic_agent.unique_id, traffic_agent.pos, traffic_agent.redLight)
            agent_id += 1

        car_pos = [(18, 4)]

    for pos in car_pos:
      car_agent = Car(agent_id, self, pos, parking_pos[5])
      self.grid.place_agent(car_agent, pos)
      self.schedule.add(car_agent)
      agent_id += 1


  def step(self):

    for trafficLight in self.schedule.agents_by_type[TrafficLight].values():
      trafficLight.step()

    for car in self.schedule.agents_by_type[Car].values():
      car.step()

    self.schedule.steps+=1

  def run_model(self, step_count=1000):
        for i in range(step_count):
            self.step()