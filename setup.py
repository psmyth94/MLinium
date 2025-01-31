from setuptools import find_packages, setup

setup(
    name="mlinium",
    version="0.1.3.dev48",
    description="A package for training mamba vision model and text encoder using CLIP",
    author_email="psmyth1994@gmail.com",
    license="Apache 2.0",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    python_requires=">=3.8.0,<3.12.0",
    install_requires=[
        "colorlog",
        "h5py",
        "scikit-learn",
        "ipython",
        "pandas",
        "tqdm",
        "ftfy",
        "regex",
        "fsspec",
        # "optuna",
        # "ray[tune]",
        # "redis",
        "mambavision",
        "huggingface_hub",
        "transformers[sentencepiece]",
        "braceexpand",
        "kaggle",
        "accelerate",
        "open_clip_torch",
    ],
    dependency_links=[
        "https://pytorch.org/get-started/locally/",
        "https://developer.nvidia.com/nccl",
    ],
    entry_points={
        "console_scripts": [
            "mlinium = mlinium.cli.main:main",
        ],
    },
)
