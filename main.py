from flask import Flask
import json
from cpu_benchmark import cpu_benchmark,check_name_cpu_benchmark
from cinbench_r23 import cinebench_r23,check_name_cinebench_r23
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/<string:benchmark>/<string:cpu_name>')
def print_bench(benchmark,cpu_name):
    cpu_benchmark()
    cinebench_r23()
    if benchmark=='cpu_benchmark':
        return check_name_cpu_benchmark(cpu_name)
    elif benchmark=='cinebench_r23':
        obj=check_name_cinebench_r23(cpu_name)
        return f'{obj}'


if __name__ == '__main__':
    app.run()