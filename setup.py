from setuptools import find_packages,setup
"""This will find all available packages within ML"""
from typing import List


HYPEN_E_DOT= 'e .'
def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirments"""

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "" )for req in requirements]
        """There will be a slash when the code is ran so I am going to remove it."""

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return requirements



setup(
    name='mlproject',
    version='0.01',
    author="Joby",
    author_email='joeb45@msn.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)
"""Writing all of the parameters required and info about the entire project,
install_requires is just installing all of the libraries I want, so I created a function
"""