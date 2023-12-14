from setuptools import setup, find_packages

setup(
    name="INITO TASK",
    version="0.1",
    author="Akash Sahu",
    author_email="akashsahu006@gmail.com",
    description="INITO Project Submission",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["os", "re", "shlex", "shutil"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
