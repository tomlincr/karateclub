import numpy as np
import networkx as nx
from karateclub import NEU, NetMF, DeepWalk


def test_neu():
    """
    Test the NEU meta embedding class.
    """
    graph = nx.newman_watts_strogatz_graph(100, 20, 0.05)

    model = NetMF()
    meta_model = NEU()
    meta_model.fit(graph, model)
    embedding = meta_model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert type(embedding) == np.ndarray

    graph = nx.newman_watts_strogatz_graph(200, 20, 0.05)

    model = DeepWalk()
    meta_model = NEU()
    meta_model.fit(graph, model)
    embedding = meta_model.get_embedding()

    assert embedding.shape[0] == graph.number_of_nodes()
    assert type(embedding) == np.ndarray
    assert np.array_equal(meta_model.fit_transform(graph, model).shape,
                          embedding.shape)

    y = embedding[:, 0]
    z, y_hat = meta_model.fit_transform(graph, model, y)
    assert y_hat.shape[0] == graph.number_of_nodes()
    assert np.array_equal(y_hat, y)
