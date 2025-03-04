import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="airflow-provider-great-expectations",
    version="0.0.6",
    author="Great Expectations",
    description="An Apache Airflow provider for Great Expectations",
    entry_points='''
        [apache_airflow_provider]
        provider_info=great_expectations_provider.__init__:get_provider_info
    ''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/great-expectations/airflow-provider-great-expectations",
    install_requires=['apache-airflow>=1.10',
                      'great-expectations>=0.13.14',
                      'pybigquery>0.3.0',
                      'SQLAlchemy>=1.3.18,<1.4'],
    packages=['great_expectations_provider',
              'great_expectations_provider.operators',
              'great_expectations_provider.example_dags'],
    python_requires='>=3.6',
    include_package_data=True
)
