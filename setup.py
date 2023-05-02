from setuptools import setup

setup(
    name='maharashtra_forts',
    version='0.3.1',
    author='Rahul Bhoyar',
    author_email='rahulbhoyaroffice@gmail.com',
    description='This is library created for all Fort Lovers in Maharashtra',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rahulbhoyar1995/maharashtra-forts-library',
    packages=['maharashtra_forts'],
    install_requires=[
        # Dependencies go here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
