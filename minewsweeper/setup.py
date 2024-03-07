from setuptools import setup, find_packages

setup(
    name='minesweeper',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'minesweeper = minesweeper.__main__:main'
        ]
    },
    install_requires=[
        # Add any dependencies here
    ],
    author='Ayush, Anmol',
    author_email='ayush.sonu@impressico.com',
    description='A command-line Minesweeper game.',
    keywords='minesweeper game command-line',
    url='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
