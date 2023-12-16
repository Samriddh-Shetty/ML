from setuptools import find_packages, setup
from typing import List

hypen = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file:
        requirements = [req.strip() for req in file.readlines()]

        if hypen in requirements:
            requirements.remove(hypen)
    return requirements

setup(
    name ="mlproject",
    version = "0.0.1",
    author ='Samriddh',
    author_email ="samshettyyyy@gmail.com",
    packages =find_packages(),
    install_requires =get_requirements("requirements.txt")
)


