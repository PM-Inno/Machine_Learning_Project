from setuptools import find_packages, setup
from typing import List

HYPEHN_E_DOT = '-e .'
def get_requirements(file_path:str)->LIst[str]:
    """
      this function return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        
        if HYPEHN_E_DOT in requirements:
            requirements.remove(HYPEHN_E_DOT)

setup(
name='machine_learning_project',
version='0.0.1',
author= 'Phumzile',
author_email= 'phumzilemadonsela75@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)