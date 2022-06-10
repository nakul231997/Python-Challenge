## CGE Python Challenge ReadMe

### This document gives an overview of how to test the challenge code

1. **Open Anaconda Prompt**

2. **Navigate to dependencies.yml file*** 
    ```python
    cd (folder path)\TechChallengePython_double\TechChallengePython\TechChallengePython\Challenge
    ```

3. **Create conda environment**
    ```python
    conda env create -f dependencies.yml
    ```
   **Update conda environment**
    ```python
    conda env update --prefix ./env --file dependencies.yml  --prune  
    ```
    
   **Activate the environment**
   ```python
    conda activate C:\Users\nakul\Downloads\TechChallengePython_double\TechChallengePython\TechChallengePython\Challenge\env
   ```
4. **Run tests**
    ```python
    python -m pytest ./test --junitxml=unit-testresults.xml --cov=src
    flake8 --output-file=lint-testresults.xml --format junit-xml
    sphinx-build -b html docs/source/ docs/build/html
    ```