import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nexstar",
    version="0.0.5",
    author="Matt Wilson",
    author_email="matt404@mswis.com",
    description="Python interface for Celestron Nexstar telescopes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matt404/nexstar",
    packages=setuptools.find_packages(),
    install_requires=['pyserial','pytz'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)