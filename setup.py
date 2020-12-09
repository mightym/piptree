from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="piptree",
    version="0.1.4",
    description="Get a dependency tree for your local requirements.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="pip requirements tree",
    url="http://github.com/mightym/piptree",
    author="Mark Wirblich",
    author_email="mark@wirblich.com",
    license="MIT",
    packages=["piptree"],
    install_requires=[
        "pip",
    ],
    include_package_data=True,
    zip_safe=False,
    scripts=["bin/piptree"],
)
