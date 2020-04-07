import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ig-data",
    version="0.0.2",
    author="Swapnanil Dutta",
    author_email="swapnanildutta2000@gmail.com",
    description="A small package to extract instagram data for the given username",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swapnanildutta/instagram-search",
    packages=setuptools.find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
