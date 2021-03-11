from string import ascii_letters
import random
import timeit
from hash_all import HashAll
import plotly.express as px


def generate_data():
    """ Creates array of strings  """
    return [''.join(random.choices(ascii_letters, k = i**4)) for i in range(1, 21)]

def calculate_time(data):
    """ Calculates the hashing duration, depending on string size  """
    h = HashAll()
    return [timeit.timeit(lambda : h.perform_hashing(text), number=1) for text in data]

def create_plot():
    """ Creates a plot showing the relationship between the amount of data and execution time """
    data = generate_data()
    time_result = calculate_time(data)

    fig = px.line(x=[len(i) for i in data], y=time_result)
    fig.update_layout(title = 'Hashing time, depending on the amount of data', xaxis_title = 'Length of text', yaxis_title='Time in seconds')
    fig.show()
