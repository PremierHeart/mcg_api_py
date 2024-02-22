from setuptools import setup

setup(
    name='mcg_api',
    version='0.9.0',
    description='Package for connecting to MCG API server',
    url='https://github.com/PremierHeart',
    #author='',
    #author_email='',
    license='Apache',
    packages=['mcg_api'],
    install_requires=['requests'],
   classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3'
    ],
)
