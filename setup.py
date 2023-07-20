from setuptools import setup

# setting up entry point, hence "run-app" from the command line would be able to invoke the main function in app.py
setup(
    name="my_project",
    version="0.1.2",
    packages=["my_project"],
    entry_points={
        "console_scripts": [
            "run-app = my_project.app:main"
        ]
    },
)