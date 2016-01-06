import random
import plotly
plotly.offline.init_notebook_mode() # run at the start of every notebook

def ydata():
    y = []
    for i in range(0, 51):
        y.append(random.randint(0, 11))
    return y    

xdata = list(range(0, 51))

def plot(x):
    plotly.offline.iplot({
        "data": [{
            "x": x,
            "y": ydata()
        },
        {
        "x" : x,
        "y" : ydata()
        }],
        "layout": {
            "title": "random data"
        }
    })

def callme():
    plot(xdata)
