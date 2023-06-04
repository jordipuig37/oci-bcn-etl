# Oci Barcelona

Very simple ETL to test and demonstrate the basic principles of testing and CI/CD. This module downloads data from the barcelona open data repository, and stores it in a SQLite database. The actual data processing has small value, and the data use case is unclear. Nevertheless, the code and the commit history serves as example of good practice regarding testing and continuous integration.

## Tests

Tests can be found in the /test folder, and a script is in place for each kind of supported test:

* Unit testing
  * Transformation testing
* Data quality
* End-to-end

Unit tests ensure that each function works as expected atomically. A separate script is provided for transformations to keep the scripts short and more domain-specific.

Data quality tests ensure the quality of the source data, including verifying that the API functions as expected and that the data conforms to the assumed schema. For data quality tests, passive checks should be implemented to verify the consistency of the data in the database and adherence to specific standards. However, these tests should not be included in the CI/CD pipeline.

The end-to-end test ensures that the pipeline runs without throwing errors. It does not validate the expected behavior and outcome, as this is accomplished by other tests.

## Continuous Integration

CI pipelines help us verify that the deployed code meets the standards defined by the tests. In this project, there are two pipelines: the first one checks the passing status of the tests, and the second one checks the code quality in terms of readability. Specifically, type hints are validated using mypy, and code style is checked using flake8.

## Roadmap

While the project has already fulfilled its purpose of providing practice with testing and CI/CD pipelines, there are opportunities to expand its functionality by incorporating the following:

* Orchestration using popular libraries like Airflow
* Introducing new transformations
* Adding new API endpoints and integrating new data
  * Refactoring the ingestion script to incorporate other software engineering best practices
* Deployment to cloud infrastructure

## Contributing

You are welcome to contribute by opening pull requests to improve the code or add new features. Feedback is also appreciated, and you can find contact information in my profile. Please note that the project's main objective is to demonstrate the testing and CI principles, and the use case itself does not aim to provide specific business value.
