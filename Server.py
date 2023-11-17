# POST, GET 
#http://127.0.0.1:500/theChallenge?name=Sergio&last=Ruiz
from model import BoidFlockers, CarsBehaivour
import mesa
from SimpleContinuousModule import SimpleCanvas


from flask import Flask, request
app = Flask(__name__)

import json

#boids = BoidFlockers()
boids = CarsBehaivour()




@app.route('/dots', methods = ['GET'])
def launchDots():
    dotsServer.launch()

def dots():
    return {"Shape": "circle", "r": 2, "Filled": "true", "Color": "Red"}


boid_canvas = SimpleCanvas(dots, 500, 500)
model_params = {
    "population": 5,
    "width": 100,
    "height": 100,
    "speed": 5,
    "vision": 10,
    "separation": 2,
}

dotsServer = mesa.visualization.ModularServer(
    CarsBehaivour, [boid_canvas], "Boids", model_params
)



#---------------------------aaaaasassdsefkjsrngjnjsrng--------------------------------------




""" 
@app.route('/theChallenge', methods = ['POST', 'GET'])
def theChallenge():
    if request.method == 'POST':
        name = request.args.get('name')
        boids.step()
        p2 = boids.getPositions()
        return "('positions :'" + str(arraysToJSON(p2)) +")"
    


    


def arraysToJSON(ar):
    result = []
    for i in ar:
        temp = []
        temp.append(i[0])
        temp.append(i[1])
        result.append(json.dumps(temp))
        #resultStr = str(result)
    return result    

"""


if __name__ == '__main__':
    dotsServer.launch(open_browser=True)
    
