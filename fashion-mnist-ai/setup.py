from setuptools import setup, find_packages
setup(
    name="fashion_mnist_ai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "matplotlib",
        "gradio",
        "scikit-learn"
    ]
)
