import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='numpy_add',
    version='0.0.3',
    author='Nasir Aziz',
    author_email='nasir.aziz@itu.edu.pk',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nasiraziz421/pip-practice',
    project_urls = {
        "Bug Tracker": "https://github.com/nasiraziz421/pip-practice/issues"
    },
    license='MIT',
    packages=['numpy_add'],
    install_requires=['requests'],
)