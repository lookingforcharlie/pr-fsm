# Policy Reporter - FSM Project

Author: Charlie Feng

## Virtual Environment

Python 3.11.4 on MacOS

## Files Structure

| File                | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| `standard_fsm.py`   | Standard implementation of a finite state machine for computing modulo 3 |
| `advanced_fsm.py`   | Advanced FSM class implementation and its usage for modulo 3 computation |
| `tests/test_fsm.py` | Unit test cases for both standard and advanced FSM implementations       |
| `pytest.ini`        | Configuration file for pytest that sets up the Python path               |
| `Dockerfile`        | Defines the Docker image for the project                                 |
| `requirements.txt`  | Lists Python dependencies                                                |

## How to run the app: Docker/Manual

### Using Docker

Make sure you have Docker installed and running on your system.

- Build the Docker image (from the project root directory):

  ```
  docker build -t pr-fsm .
  ```

- Run the tests using the Docker container:

  ```
  docker run --rm pr-fsm
  ```

- Run the standard FSM script using the Docker container:

  ```
  docker run --rm pr-fsm python standard_fsm.py
  ```

- Run the advanced FSM script using the Docker container:

  ```
  docker run --rm pr-fsm python advanced_fsm.py
  ```

- Get an interactive shell inside the container:
  ```
  docker run --rm -it pr-fsm /bin/bash
  ```
  (To exit the shell, type `exit` and press Enter, or press `Ctrl+D`)

### Using Python (Virtual) Environment

- Install the dependencies (from the project root directory)

  ```
  pip install -r requirements.txt
  ```

- Run tests (from the project root directory)

  Run all tests:

  ```
  pytest
  ```

  Run only standard FSM tests:

  ```
  pytest tests/test_fsm.py::TestStandardFSM
  ```

  Run only advanced FSM tests:

  ```
  pytest tests/test_fsm.py::TestAdvancedFSM
  ```

- Run standard and advanced fsm respectively

  ```
  python3 standard_fsm.py
  ```

  ```
  python3 advanced_fsm.py
  ```
