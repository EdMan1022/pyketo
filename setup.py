import setuptools

with open("README.md", "r") as file_obj:
    long_description = file_obj.read()

packages = setuptools.find_packages()

setuptools.setup(
    name='Pyketo',
    version='0.1dev',
    author="Edward Brennan",
    author_email="EdMan1022@gmail.com",
    description="A Python implementation of the Marketo API",
    long_description=long_description,
    url="https://github.com/EdMan1022/pyketo.git",
    packages=packages,
    install_requires=["requests"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
