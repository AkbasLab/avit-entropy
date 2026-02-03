import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="avit-entropy",
    version="1.0.1",
    author="Quentin Goss, Dr. Mustafa Ilhan Akbas",
    author_email="gossq@my.erau.edu, akbasm@erau.edu",
    description="A python module for calculating entropy of autonous vehicle scenarios using information theory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AkbasLab/avit-entropy",
    project_urls={
        "Bug Tracker": "https://github.com/AkbasLab/avit-entropy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">= 3.9",
    install_requires=[
        "sim-bug-tools",
        "shapely"
    ],
)