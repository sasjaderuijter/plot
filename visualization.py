#!/usr/bin/env python3
import os
import sys
import yaml

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn

def create_plot(file: str) -> str:
  # Read regression data in
  data = pd.read_csv(f"{file}.csv", sep=';')

  confusion_matrix = pd.crosstab(data["Actual"], data["Prediction"], rownames=["Actual"], colnames=["Prediction"])
  sn.heatmap(confusion_matrix, annot=True)

  output_loc = "/data/confusion_matrix.png"
  plt.savefig(output_loc)

  return output_loc

def create_boxplot(file: str) -> str:
  data = pd.read_csv(f"{file}.csv", sep=';')

  data.boxplot()

  output_loc = "/data/boxplot.png"
  plt.savefig(output_loc)

if __name__ == "__main__":
  command = sys.argv[1]
  argument = os.environ["FILE"]
  functions = {
    "create_plot": create_plot,
    "create_boxplot": create_boxplot,
  }
  output = functions[command](argument)
  print(yaml.dump({"output": output}))