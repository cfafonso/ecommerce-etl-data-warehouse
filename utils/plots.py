
import os
import seaborn as sns
import matplotlib.pyplot as plt


def create_count_plot(data, variable, labels, size, title, save=False, path=None, outfile=None):
    """
    Creates a plot showing the absolute frequency distribution for the specified variable.

    Args:
        data (pandas.DataFrame): the dataframe containing the variable to plot.
        variable (str): the name of the variable to create the count plot for.
        labels (list): list where the first element is the x-axis label and the second element is the y-axis label.
        size (tuple): figure size as (width, length).
        title (str): the title of the plot.
        save (boolean): True to save the plot to a file or False otherwise.
        path (str, optional): directory path where to save the plot. Required if save is True.
        outfile (str, optional): name of the file that contains the plot. Required if save is True.
    """

    plt.figure(figsize=size)
    sns.countplot(data=data, x=variable)
    plt.xticks(rotation=45)
    plt.xticks(horizontalalignment='right', fontweight='light', fontsize='x-large')
    plt.tight_layout()
    plt.title(title, fontsize=22, weight='bold', y=1.05)
    plt.xlabel(labels[0], fontsize=20)
    plt.ylabel(labels[1], fontsize=20)

    if save and path and outfile:
        os.makedirs(path, exist_ok=True)
        plt.savefig(f"{path}{outfile}.png", bbox_inches='tight', dpi=300)

    plt.show()


def create_violin_plot(data, variables, labels, size, title, save=False, path=None, outfile=None):
    """
    Creates a violin plot showing the distribution of a numerical variable.
    
    Args:
        data (pandas.DataFrame): the dataframe containing the variables to plot.
        variables (list): list where the first element corresponds to the x variable (numerical) and the second
                          element corresponds to the y variable (categorical).
        labels (list): list where the first element is the x-axis label and the second element is the y-axis label.
        size (tuple): figure size as (width, length).
        title (str): the title of the plot.
        save (boolean): True to save the plot to a file or False otherwise.
        path (str, optional): directory path where to save the plot. Required if save is True.
        outfile (str, optional): name of the file that contains the plot. Required if save is True.
    """

    plt.figure(figsize=size)
    sns.violinplot(data=data, x=variables[0], y=variables[1])
    plt.xticks(rotation=0)
    plt.title(title, fontsize=16, weight='bold', y=1.05)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    
    if save and path and outfile:
        os.makedirs(path, exist_ok=True)
        plt.savefig(f"{path}{outfile}.png", bbox_inches='tight', dpi=300)

    plt.show()