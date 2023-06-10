AMS Data Processor
=================

The AMS Data Processor is a Python script that allows you to process AMS measurement files by applying mathematical formulas to the data. It extracts analysis records from the file, performs specified mathematical operations, and generates HTML output files with the modified data.

Features
--------

- Reads AMS measurement files and extracts analysis records.
- Applies various mathematical formulas to the data, including sum, division, multiplication, square root, subtraction, and natural logarithm.
- Generates HTML output files with the modified data in a tabular format.

Setup
-----

To set up the project, run the following command:

.. code-block:: bash

   make setup

Pylint
------

To run Pylint for code analysis, use the following command:

.. code-block:: bash

   make pylint

Run All Tests with Coverage
---------------------------

To run all tests with coverage report, use the following command:

.. code-block:: bash

   make test

Run Pre-commit Hooks
--------------------

To run pre-commit hooks, including Pylint and other linting tools, use the following command:

.. code-block:: bash

   pre-commit run --all-files

Jenkins CI/CD Pipeline
----------------------

A sample Jenkinsfile is included that can be used for the pipeline on platforms like Bitbucket.

Usage
-----

To run the AMS Data Processor, use the following command-line syntax:

.. code-block:: bash

   ams_data_processor.py inputs/C14_setting.ams sum output

Please note that the above command assumes the script name is ``ams_data_processor.py``, and the input file is located in the provided path.

Technology Stack & Features
---------------------------

- Panda
- Numpy
- cProfile
- Dependency graph
- pylint
- Pre-commit
- Test coverage report
- Docker with Docker Compose
- Makefile
- Logs
- Jenkins CI/CD Pipeline
- Kubernetes
- Design patterns (Pub-Sub, Command, Repository, Singleton)
- Layer architecture (DDD)

DDD and Layer Architecture
--------------------------

The project follows the Domain Driven Design (DDD) with the Layer architecture. To see the architecture graph, run the following command:

.. code-block:: bash

   make profile-graph-cluster

.. image:: https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/77e7498e-05fd-4d78-8e5f-e95b0098ce55
   :alt: profile_graph_cluster

Full Dependency Graph
---------------------

To see the full dependency graph, run the following command:

.. code-block:: bash

   make profile-graph

.. image:: https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/ecff1848-9636-4e7c-b915-ca8f935afc79
   :alt: ams_data_processor

Call-graph to Improve Performance
---------------------------------

If you want to see which parts of the code are taking the most time (the bottleneck), run the following command:

.. code-block:: bash

   make profile

.. image:: https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/30dc8de3-1a56-40f5-84e1-43dff827b0be
   :alt: Screenshot 2023-06-10 at 12 15 30 PM

Test Coverage
-------------

To run all tests and see the test coverage report, run the following command:

.. code-block:: bash

   make test

.. image:: https://github.com/omerahmed41/AMS_Data_Processor_Numpy/assets/15717941/9cf06a03-3058-497d-92f7-3a5bf4752b2a
   :alt: Screenshot 2023-06-10 at 12 18 08 PM
