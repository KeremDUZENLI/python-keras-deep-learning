# Deep Learning Examples with Keras

A collection of deep learning examples using Keras, covering neural networks, recommender systems, convolutions, and object detection. Based on the course **Advanced Machine Learning**, University of Debrecen.

## GitHub Repository (Standalone Version)

You can access the non-Colab version of the project directly on GitHub:

[github.com/KeremDUZENLI/python-keras-deep-learning](https://github.com/KeremDUZENLI/python-keras-deep-learning)

## Install

1. Download Python 3.6.8: [Python 3.6.8 Download](https://www.python.org/downloads/release/python-368/)
2. Check Python versions installed: `py -0`
3. Check the default version: `python --version`
4. Select Python 3.6.8: [Video Guide](https://www.youtube.com/watch?v=C5mn0WWKmGY&t=10s)

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/KeremDUZENLI/python-keras-deep-learning.git
   ```
2. Create a virtual environment:
   ```sh
   python -m venv myEnv
   ```
3. Activate the virtual environment:
   - **Windows**: `myEnv\Scripts\activate`
   - **Linux/macOS**: `source myEnv/bin/activate`
4. Update pip:
   ```sh
   python -m pip install --upgrade pip
   ```
5. Update setuptools:
   ```sh
   pip install --upgrade setuptools
   ```
6. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
7. Freeze dependencies (optional):
   ```sh
   python -m pip freeze > requirements.txt
   ```

## Notebooks

1. Install Jupyter:
   ```sh
   pip install jupyterlab
   ```
2. Launch Jupyter:
   ```sh
   jupyter lab
   ```

### Notebook Descriptions

- [1. Neural Networks](notebooks/1_neural_networks.ipynb) – Basics of neural networks with Keras.
- [2. Backpropagation](notebooks/2_backpropagation.ipynb) – Understanding the backpropagation algorithm and its implementation in Keras.
- [3. Neural Recommender](notebooks/3_neural_recommender.ipynb) – Building a simple recommender system using neural networks.
- [4. Convolutional Networks](notebooks/4_convolutional_network.ipynb) – Introduction to convolutional neural networks (CNNs) for image classification.
- [5. Fully Convolutional Networks](notebooks/5_full_convolutional_network.ipynb) – Implementing a full convolutional network for image segmentation tasks.
- [6. CNN Classification](notebooks/6_convolutional_network_classification.ipynb) – Classifying images using a convolutional neural network.
- [7. Text Classification & Seq2Seq Translation](notebooks/7_text_classification_seq2seq_translation.ipynb) – Text classification using RNNs and sequence-to-sequence models for language translation.
- [8. Variational Autoencoders](notebooks/8_variational_autoencoders.ipynb) – Implementing variational autoencoders for generative modeling.

## Acknowledgments

This project is based on the **Advanced Machine Learning** course at the **University of Debrecen**

- **Prof. Dr. András Hajdu** – Dean, Head of Department

  - _Department of Data Science and Visualization, Faculty of Informatics, University of Debrecen_
  - Email: [hajdu.andras@inf.unideb.hu](mailto:hajdu.andras@inf.unideb.hu)

- **Dr. Balázs Harangi** – Associate Professor, Deputy Head of Department

  - _Department of Data Science and Visualization, Faculty of Informatics, University of Debrecen_
  - Email: [harangi.balazs@inf.unideb.hu](mailto:harangi.balazs@inf.unideb.hu)

- **Kerem Düzenli** – PhD Candidate, University of Debrecen

  - _Creator and maintainer of this repository_
  - Email: [kerem.duzenli@inf.unideb.hu](mailto:kerem.duzenli@inf.unideb.hu)

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b YourBranch
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```sh
   git push origin YourBranch
   ```
5. Open a pull request.

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. This means you are free to:

- **Share** – Copy and redistribute the material in any medium or format.
- **Adapt** – Remix, transform, and build upon the material.

However, **you may not use the material for commercial purposes**.

For details, see the [LICENSE](LICENSE) file or read more at [Creative Commons](https://creativecommons.org/licenses/by-nc/4.0/).

## Disclaimer

This repository is intended **only for educational and research purposes**. The authors and contributors assume no responsibility for misuse of the code or any implications arising from its use.

## Support My Work

If you find this resource valuable and would like to help support my education and doctoral research, please consider treating me to a cup of coffee (or tea) via Revolut.

<div align="center">
  <a href="https://revolut.me/krmdznl" target="_blank">
    <img src="https://img.shields.io/badge/Support%20My%20Projects-Donate%20via%20Revolut-orange?style=for-the-badge" alt="Support my education via Revolut" />
  </a>
</div> <br>
