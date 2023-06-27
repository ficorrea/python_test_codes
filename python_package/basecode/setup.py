from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Meu primeiro pacote em Python'
LONG_DESCRIPTION = 'Meu primeiro pacote em Python com uma descrição um pouco mais longa'

# Setting up
setup(
       # 'name' deve corresponder ao nome da pasta 'verysimplemodule'
        name="simplecode", 
        version=VERSION,
        author="Felipe Corrêa",
        author_email="<felipe@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # adicione outros pacotes que 
        # precisem ser instalados com o seu pacote. Ex: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows"
        ]
)