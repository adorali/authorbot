from histograms import Dictogram


def make_higher_order_markov_model(order, data):
    markov_model = dict()

    for i in range(0, len(data)-order):
        # Create the window
        window = tuple(data[i: i+order])
        # Add to the dictionary
        if window in markov_model:
            # We have to just append to the existing Dictogram
            markov_model[window].update([data[i+order]])
        else:
            markov_model[window] = Dictogram([data[i+order]])
    return markov_model
