from setuptools import setup

setup(
    name='Maven Version Comparator',
    version='1.0',
    description='Compare maven release versions',
    url='https://github.com/suru33/maven-version-comparator',
    author='SuRu',
    author_email='33urus@gmail.com',
    license='GPLv3+',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    py_modules=[
        'cli', 'maven_version'
    ],
    entry_points={
        'console_scripts': [
            'mvn-compare=cli:main',
        ],
    },
)