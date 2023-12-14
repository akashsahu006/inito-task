from setuptools import setup, find_packages

setup(
    name="your_package_name",  # Replace with your package's name
    version="0.1",  # Package version
    author="Akash Sahu",  # Replace with your name
    author_email="akashsahu006@gmail.com",  # Replace with your email
    description="INITI Project Submission",  # Provide a short description
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # If you have a README.md, otherwise remove this line
    url="http://github.com/yourusername/your_package",  # Replace with the URL of your package
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        # List your package dependencies here. Example:
        # 'numpy>=1.18.1',
        # 'pandas>=1.0.3',
    ],
    classifiers=[
        # Choose classifiers from https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum version requirement of the package
    # entry_points={
    #     'console_scripts': [
    #         # If your package has executable scripts, define them here. Example:
    #         # 'script_name = package.module:function',
    #     ],
    # },
)
