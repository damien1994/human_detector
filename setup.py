from setuptools import setup


REQUIREMENTS = [
    'numpy==1.20.2',
    'opencv-python==4.5.1.48',
    'pafy==0.5.5',
    'youtube-dl==2021.4.1'
]

setup(
    name='human_detector',
    author='Damien Michelle',
    author_email='damienmichelle1994@hotmail.com',
    version='1.0',
    packages=['human_detector'],
    include_package_data=True,
    python_requires='~=3.7',
    install_requires=REQUIREMENTS,
    description='Real-time application in order to detect humans in video',
    license='LICENSE',
    entry_points={
        'console_scripts': ['human_detector=human_detector.main:main']
    },
    long_description=open('README.md').read()
)