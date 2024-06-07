# time tracker (backend)

This Django application is designed to help users efficiently track and manage their worked hours. 


### how to run (steps):
- `git clone git@github.com:smdirr/rest_api.git` 
- `python3 -m venv .venv` create virtual env
- `source .venv/bin/activate` activate virtual env
- `tox` execute lint, tests and coverage

    ```
    ----------------------------------------------
    TOTAL                         80      0   100%
    py310: commands[2]> coverage html
    Wrote HTML report to htmlcov/index.html
    py310: OK ✔ in 2.54 seconds
    lint: commands[0]> flake8 .
    py310: OK (2.54=setup[0.07]+cmd[2.18,0.13,0.16] seconds)
    lint: OK (0.22=setup[0.01]+cmd[0.21] seconds)
    congratulations :) (2.82 seconds)

    ```