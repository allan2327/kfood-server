import numpy as np
import tensorflow as tf
from django.conf import settings


def create_graph(pb_file):
    """
    Creates a graph from saved GraphDef file and returns a saver.
    """
    # Creates graph from saved graph_def.pb.
    with open(pb_file, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')


# Prepare tensorflow
sess = tf.Session()
create_graph(settings.KFOOD_PB_FILE)
with open(settings.KFOOD_LABELS_FILE, 'r') as f:
    labels = list(map(str.strip, f.readlines()))


def classify(image_data):
    softmax_tensor = sess.graph.get_tensor_by_name(
        settings.KFOOD_FINAL_TENSOR)
    scores = np.squeeze(
        sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data}))
    return labels[scores.argmax()]
