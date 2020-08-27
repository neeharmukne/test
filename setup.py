#!/usr/bin/env python

from distutils.core import setup

setup(name='test',
      version='1.0',
      description='Python NLP Funcationalities',
      author='Data Science',
      #author_email='',
      #url='',
      packages=['test'],
      install_requires=['numpy==1.18.1',
                        'tensorflow==2.0.0a0',
                        'pandas==0.25.3',
                        'beautifulsoup4==4.6.0',
                        'nltk==3.3',
                        'tensorflow-estimator==2.2.0',
                        'tensorflow-addons==0.10.0',
                        'gensim==3.8.1',
                        'transformers==2.10.0',
                        'datefinder==0.7.1',
                        'scikit-learn==0.21.3']
     )
