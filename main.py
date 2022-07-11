from flask import Flask
from flask_restful import Api,Resource,reqparse
import json
from cpu_benchmark import cpu_benchmark,check_name_cpu_benchmark
from cinbench_r23 import cinebench_r23,check_name_cinebench_r23

app=Flask(__name__)
api=Api(app)

class Contest(Resource):
    def get(self,benchmark,cpu_name):
        cpu_benchmark()
        cinebench_r23()
        if benchmark == 'cpu_benchmark':
            return check_name_cpu_benchmark(cpu_name)
        elif benchmark == 'cinebench_r23':
            obj = check_name_cinebench_r23(cpu_name)
            return f'{obj}'


api.add_resource(Contest, "/api/<string:benchmark>/<string:cpu_name>")


if __name__ == '__main__':
    app.run()