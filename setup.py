from setuptools import find_packages,setup
from typing import List
HYPENDOT="-e ."
def get_requirements(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]
        if(HYPENDOT in requirement):
            requirement.remove(HYPENDOT)
    return requirement


setup(
    name='mlproject',
    version='0.0.1',
    author='Ranjit Vhanmane',
    author_email='vhanmaneranjit80.gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )