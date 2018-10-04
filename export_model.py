#!/usr/bin/enb python3

import tensorflow as tf
from tensorflow.python import saved_model
from tensorflow.python.saved_model.tag_constants import SERVING
from tensorflow.python.saved_model.signature_constants import DEFAULT_SERVING_SIGNATURE_DEF_KEY
from tensorflow.python.saved_model.signature_def_utils_impl import predict_signature_def
import shutil


def export_keras_model(m, export_path):
    builder = saved_model.builder.SavedModelBuilder(export_path)
    signature = predict_signature_def(inputs={'input': m.inputs[0]},
                                      outputs={'sentiment': m.outputs[0]})
    
    with tf.keras.backend.get_session() as sess:
        builder.add_meta_graph_and_variables(
            sess=sess,
            tags=[SERVING],
            signature_def_map={
                DEFAULT_SERVING_SIGNATURE_DEF_KEY: signature
            }
        )
        builder.save()


if __name__ == '__main__':
    tf.keras.backend.set_learning_phase(0)
    tf_model = tf.keras.models.load_model('keras_model.hdf5')
    try:
        shutil.rmtree('out')
    except FileNotFoundError:
        pass
    export_keras_model(tf_model, 'out/')
