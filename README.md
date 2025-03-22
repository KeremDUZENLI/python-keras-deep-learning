# Deep Learning Examples with Keras

A collection of deep learning examples using Keras, covering neural networks, recommender systems, convolutions, and object detection. Based on the course Advanced Machine Learning, University of Debrecen.

## Install

1. Download Python 3.6.8: `https://www.python.org/downloads/release/python-368/`
2. Check Python versions installed: `py -0`
3. Check the default version: `python --version`
4. Select Python 3.6.8: `https://www.youtube.com/watch?v=C5mn0WWKmGY&t=10s`

## Setup

1. Clone the repo: `git clone https://github.com/KeremDUZENLI/python-keras-deep-learning.git`
2. Create a virtual environment: `python -m venv myEnv`
3. Activate it (windows): `myEnv\Scripts\activate` | Activate it (linux): `source myEnv/bin/activate`
4. Update pip: `python -m pip install --upgrade pip`
5. Update setuptools: `pip install --upgrade setuptools`
6. Install dependencies: `pip install -r requirements.txt`
7. Freeze dependencies: `python -m pip freeze > requirements.txt`

## Notebooks

1. Install Jupyter: `pip install jupyterlab`
2. Launch Jupyter: `jupyter lab`

### Notebook Descriptions

- (notebooks/1_neural_networks.ipynb) : Basics of neural networks with Keras.
- (notebooks/2_backpropagation.ipynb) : Understanding the backpropagation algorithm and its implementation in Keras.
- (notebooks/3_neural_recommender.ipynb) : Building a simple recommender system using neural networks.
- (notebooks/4_convolutional_network.ipynb) : Introduction to convolutional neural networks (CNNs) for image classification.
- (notebooks/5_full_convolutional_network.ipynb) : Implementing a full convolutional network for image segmentation tasks.
- (notebooks/6_convolutional_network_classification.ipynb) : Classifying images using a convolutional neural network.
- (notebooks/7_1_text_classification.ipynb) : Text classification using recurrent neural networks (RNNs).
- (notebooks/7_2_seq2seq_translation.ipynb) : Sequence-to-sequence models for language translation tasks.
- (notebooks/8_variational_autoencoders.ipynb) : Implementing variational autoencoders for generative modeling.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Make your changes and commit them: `git commit -m "Add some feature"`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.
