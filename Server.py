import mesa

from model import CarBehaivour
from SimpleContinuousModule import SimpleCanvas


def car(agent):
    return {"Shape": "circle", "r": 2, "Filled": "true", "Color": "Red"}


boid_canvas = SimpleCanvas(car, 500, 500)
model_params = {
    "population": 5,
    "width": 100,
    "height": 100,
    "speed": 5,
    "vision": 10,
    "separation": 2,
}

server = mesa.visualization.ModularServer(
    CarBehaivour, [boid_canvas], "Boids", model_params
)

if __name__ == '__main__':
    server.launch(open_browser=True)
    