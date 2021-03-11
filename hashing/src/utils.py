from string import ascii_letters
import random
import timeit
from hash_all import HashAll
import plotly.express as px


def generate_data():
    return [''.join(random.choices(ascii_letters, k = i**4)) for i in range(1, 21)]

def create_plot():
    data = generate_data()
    results = []
    h = HashAll()

    for text in data:
        results.append(timeit.timeit(lambda: h.perform_hashing(text), number=1))

    fig = px.line(x=[len(i) for i in data], y=results)
    fig.update_layout(title = 'Hashing time, depending on the amount of data', xaxis_title = 'Length of text', yaxis_title='Time in seconds')
    fig.show()
