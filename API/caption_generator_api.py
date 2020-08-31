import caption_generator
from flask import (
    Flask
)
from PIL import Image
import requests
import urllib.request
import json
import tensorflow as tf
from keras.applications.vgg16 import VGG16
from keras.models import Model

url = "https://dog.ceo/api/breeds/image/random"

# Create the application instance
app = Flask(__name__)

@app.route('/')
def jokemodel():
    print("----- jokemodel")

    r = requests.get(url).json()
    photo_url = r["message"]

    print(photo_url)

    with urllib.request.urlopen(photo_url) as photo:
        with open('temp.jpg', 'wb') as f:
            f.write(photo.read())

    # img = Image.open('temp.jpg')
    print("----- jokemodel: Generate temp.jpg")
    caption = caption_generator.generate_caption(VGG16_model, model, tokenizer, 'temp.jpg')

    print("----- jokemodel: Send json")
    data = {
        "caption": caption,
        "image_url": photo_url
    }

    return json.dumps(data)

# Run the application when in stand alone
if __name__ == '__main__':
    config = tf.compat.v1.ConfigProto(gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.8))
    config.gpu_options.allow_growth = True
    session = tf.compat.v1.Session(config=config)
    tf.compat.v1.keras.backend.set_session(session)

    model, tokenizer = caption_generator.init_generator()

    # load the model
    VGG16_model = VGG16()

    # re-structure the model
    VGG16_model.layers.pop()
    VGG16_model = Model(inputs = VGG16_model.inputs, outputs = VGG16_model.layers[-1].output)

    app.run(debug = True)
