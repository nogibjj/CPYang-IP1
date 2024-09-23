[![Format](https://github.com/nogibjj/CPYang-IP1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/CPYang-IP1/actions/workflows/format.yml)

[![Install](https://github.com/nogibjj/CPYang-IP1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/CPYang-IP1/actions/workflows/install.yml)

[![Lint](https://github.com/nogibjj/CPYang-IP1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/CPYang-IP1/actions/workflows/lint.yml)

[![Test](https://github.com/nogibjj/CPYang-IP1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/CPYang-IP1/actions/workflows/test.yml)

## Houseprice Analysis Project

This project provides some barebones analysis framework for any dataframe, using the Californian House Price data as an example.

Simply run `make all` to run the analysis and generate the reports. 


## Demo

Demo Video is here: 

## Project Structure:
- Makefile: Contains commands to build, test, deploy and generates the report in the project
- main.py contains the main analysis that creates the figures and analysis
- requirements.txt contains the main libraries requirements
- test_main.py contains the tests for the main functions
- test_lib.py contains the tests for the helper functions in mylib
- train.csv is the main data we're using here
- .devcontainer contains the Dockerfile and the devcontainer.json file for container environment

## Analysis

We can see the distribution of id's in the housing data
 ![Figure](hist.png)

There's also a histogram of the age of the houses.

![Age Histogram](hist_HouseAge.png)



