# pytest-indigo
pytest-indigo is a testing frame work that is designed to allow IndigoDomo plugins to be tested without having access to an Indigo Server.
The primary use case is in CI/CD applications.

## What this project is, will be, or hopes to be
### An Indigo mocking tool
This will inject an object into the Python `sys.modules` object that will let your plugin *think* it is running in an Indigo Server environment.

## What this project isn't
### A functional Indigo Server
This is a testing utility.

### A 1:1 replication of Indigo
I will try my best to **mimic** Indigo Server behavior, but this will never be perfect.
