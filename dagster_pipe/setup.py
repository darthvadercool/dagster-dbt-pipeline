import setuptools

setuptools.setup(
    name="dagster_pipe",
    packages=setuptools.find_packages(exclude=["dagster_pipe_tests"]),
    install_requires=[
        "dagster==0.15.7",
        "dagit==0.15.7",
        "pytest",
    ],
)
