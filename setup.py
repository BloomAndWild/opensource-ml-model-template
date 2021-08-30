import setuptools

install_requires = [
    "numpy",
]

setuptools.setup(
    name="opensource-ml-model-template",
    version="0.1",
    description="Template for ML model",
    url="https://github.com/BloomAndWild/opensource-ml-model-template",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["data/*", "queries/*"]},
    install_requires=install_requires,
    zip_safe=False,
)