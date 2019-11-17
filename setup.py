from distutils.core import setup

REQUIRED = ['protobuf',  'numpy', 'tqdm']
setup(
    name='reversegoogle',
    version='0.1.0',
    packages=['reversegoogle'],
    install_requires=REQUIRED,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)