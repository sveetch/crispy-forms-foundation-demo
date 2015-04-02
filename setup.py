from setuptools import setup, find_packages

setup(
    name='crispy-forms-foundation-demo',
    version=__import__('crispy_forms_foundation_demo').__version__,
    description=__import__('crispy_forms_foundation_demo').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='sveetch@gmail.com',
    url='http://pypi.python.org/pypi/crispy-forms-foundation-demo',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'crispy-forms-foundation >= 0.5.0'
    ],
    include_package_data=True,
    zip_safe=False
)