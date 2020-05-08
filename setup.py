import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

libs = [line.rstrip('\n') for line in open('requirements.txt')]

setuptools.setup(
    name="groundhopping-entities-sdk",
    version='1.0.0',
    author="Guillaume Dormoy",
    author_email="dormoy.guillaume@gmail.com",
    description="A set of module for providing a common way of working with external components",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pa-groundhopping-lambda/groundhopping-entities",
    packages=setuptools.find_packages(),
    install_requires=libs,
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)