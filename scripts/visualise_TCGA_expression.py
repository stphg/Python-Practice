"""
Script: visualise_TCGA_expression.py
Purpose: Generates scatter and box plots for TCGA expression data.
Dependencies: numpy, matplotlib, pandas
"""

import numpy as np
import matplotlib.pyplot as plt

def scatter_expression(df, col_x, col_y):
    """
    Generates a scatter plot of log2-transformed gene expression values.
    
    Parameters:
    df (pd.DataFrame): Dataframe containing expression data
    col_x (str): Column name for x-axis
    col_y (str): Column name for y-axis
    """
    x = np.log2(df[col_x] + 1)
    y = np.log2(df[col_y] + 1)

    fig, ax = plt.subplots(figsize=(10,5))
    ax.scatter(x, y, c="pink")
    ax.set(xlim=(0,20), xticks=np.arange(0,21),
           ylim=(0,20), yticks=np.arange(0,21))
    plt.title(f"Scatter plot of {col_x} vs {col_y}")
    plt.xlabel(f"log2({col_x}) expression")
    plt.ylabel(f"log2({col_y}) expression")
    plt.show()

def boxplot_expression(df, value_col, group_col):
    """
    Generates a boxplot of log2-transformed expression by group.
    
    Parameters:
    df (pd.DataFrame): Dataframe containing expression data
    value_col (str): Column name of expression values
    group_col (str): Column name of grouping variable
    """
    df[f"{value_col}_log2"] = np.log2(df[value_col] + 1)
    fig, ax = plt.subplots(figsize=(8,8))
    df.boxplot(column=f"{value_col}_log2", by=group_col, ax=ax, grid=False, patch_artist=True)
    plt.suptitle('')
    plt.title(f"log2-transformed {value_col} Expression by {group_col}")
    plt.xlabel(group_col)
    plt.ylabel(f"log2({value_col}) Expression")
    plt.show()
