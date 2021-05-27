# Plot
_Universiteit van Amsterdam - Web Services and Cloud-Based Systems: assignment 5_

This Brane package is used as the visualisation of the pipeline.
It uses the output of the Brane packages create_prediction and etl.

## Installation
Import the package as follows:
```shell
$ brane import sasjaderuijter/plot
```
## Running package
Create a confusion matrix, using the example dataset _regression_results.csv_
```shell
create_plot("/data/regression_results")
```

Create a boxplot, using the example dataset _titanic_trainset.csv_
```shell
create_boxplot("/data/titanic_trainset")
```
