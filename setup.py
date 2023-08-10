from setuptools import find_packages,setup
from typing import List

HYPEN_e_DOT='-E.'
def get_requirements(file_path:str)->List[str]:

#tis function will return the list of requirements

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","")for req in requirements]

        if HYPEN_e_DOT in requirements:
            requirements.remove(HYPEN_e_DOT)  #this is to remove the -e. not to be rad along the other text


setup(
    name='mlproject',
    version='0.0.1',
    author='apurba_chakma',
    author_email='ac872013@student.nitw.ac.in',
    pakages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)