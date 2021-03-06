from selfmade_resnetmodel.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.utils.vis_utils import plot_model
import numpy as np

from  normalization_layers.GroupNormalization import GroupNormalization

model = ResNet50(weights='imagenet')

# GroupNormalization(axis=-1, epsilon=1e-6, group=32, **kwargs)

print(model.summary())

# plot_model(model, to_file='model_plot1.png', show_shapes=True, show_layer_names=True)


# img_path = 'elephant.jpg'
# img = image.load_img(img_path, target_size=(224, 224))
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)
# preds = model.predict(x)
# # decode the results into a list of tuples (class, description, probability)
# # (one such list for each sample in the batch)
# print('Predicted:', decode_predictions(preds, top=1)[0][0][1])
# # Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]
