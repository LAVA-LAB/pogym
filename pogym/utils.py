def sample_from(distribution, np_random):
    return np_random.multinomial(1, distribution).argmax()
