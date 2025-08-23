import os 
from setuptools import find_packages,setup 
from typing import List

# function to read all dependencies from requirements.txt
def get_requirements()-> List[str]:
    requirements_lst:List[str]=[]

    try:
        with open("requirements.txt","r")as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)
    
    except FileNotFoundError:
        print(f"requirements.txt is not found......")
    
    return requirements_lst

# setup config for package
setup(
    version="0.0.1",
    author="mayur",
    packages=find_packages(), # automatically finds all Python packages
    install_requires=get_requirements() # install dependencies from requirements.txt
)
