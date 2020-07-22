from setuptools import setup, find_packages

setup(
    name='RapsberryPy',
    version='1.0.0',
    url='https://github.com/Shaofanl/RaspberryPy.git',
    author='ShaoFanl',
    author_email='author@gmail.com',
    description='Python toolkits for Raspberry Pi Model 3 B',
    packages=find_packages(),    
    install_requires=['flask >= 1.1.2', 'pySerial >= 3.4', 'enum34 >=1.1.10'],
)
