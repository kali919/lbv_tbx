from setuptools import setup, find_packages

# Lire le contenu de README.md pour la description longue
def read_long_description():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='lbv_tbx',
    version='0.1.0',
    description='A library to support daily team analysis',
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
    author='Kali Mohamed Taha',
    author_email='kalimohamedtaha@gmail.com',
    license='MIT',
    url='https://github.com/kali919/lbv_tbx',
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=[
        'pyspark',
    ],
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    include_package_data=True,
)
