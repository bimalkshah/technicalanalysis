from setuptools import setup, find_packages

setup(
    name="tech_analysis",
    version="0.1.0",
    author="Bimal Kumar Shah",
    author_email="shah.bimal005@gmail.com",
    description="Pure Python technical analysis package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/tech_analysis",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
