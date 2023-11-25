import mesa
from agents import Street, Building, TrafficLight, ParkingSpace, Car
from model import TrafficModel

def car_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Car:
        portrayal["Shape"] = "resources/car.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2


    if isinstance(agent, Street):
        portrayal["Shape"] = "resources/street.png"
        portrayal["scale"] = 0.9
        portrayal["Color"] = "White"
        portrayal["Layer"] = 0
        #portrayal["Filled"] = True

    if isinstance(agent, Building):
        portrayal["Shape"] = "resources/building.png"
        portrayal["scale"] = 0.9
        portrayal["Color"] = "orange"
        portrayal["Layer"] = 1
        #portrayal["Filled"] = True

    if isinstance(agent, ParkingSpace):
        portrayal["Shape"] = "resources/parking.jpeg"
        portrayal["scale"] = 0.9
        portrayal["Color"] = "yellow"
        portrayal["Layer"] = 1
        portrayal["Filled"] = True

    if isinstance(agent, TrafficLight):
        portrayal["Shape"] = "resources/red.png" if agent.redLight else "resources/green.png"
        portrayal["scale"] = 0.9
        portrayal["Color"] = "Red" if agent.redLight else "Green"
        portrayal["Layer"] = 1
        portrayal["Filled"] = True

    return portrayal

canvas_element = mesa.visualization.CanvasGrid(car_portrayal, 24, 24, 500, 500)



server = mesa.visualization.ModularServer(
    TrafficModel, [canvas_element], "Traffic Model"
)

if __name__ == '__main__':
    server.launch(open_browser=True)