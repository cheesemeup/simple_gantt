# simple_gantt.py
# Author: cheesemeup

"""This script generates a very simple gantt chart, based on the configuration in the runscript.

The intended resolution is in months, to provide a rough outline for work packages in multi-yeat projects
"""

import matplotlib.pyplot as plt

def simple_gantt():
    # get config
    # config = get_config()

    # make chart
    make_chart()


def get_config():
    """Get the config for the gantt chart specified in the runscript

    Returns:
        config
    """
    return config


def make_chart():
    """Create and save the chart

    Args:
        config
    """
    # open figure
    fig = plt.figure()

    # zoom based on the number of tasks and months
    # plt.xlim = ([0,max(max(config.work_packages))])
    # plt.ylim = ([0.5,len(config.work_packages)+0.5])

    # title
    # plt.title(config.figure_title)

    # create axis labels, note that order is inverted
    # ytick_position, ytick_label = generate_yticks()
    # plt.yticks = (ytick_position, ytick_label)
    # xtick_position, xtick_label = generate_xticks()
    # plt.xticks = (xtick_position, xtick_label)


    # create boxes, note that order is inverted


    # save figure
    plt.savefig(f"out/config.figure_name.png")
    plt.close()


def generate_yticks():
    pass


def generate_xticks():
    pass


if __name__ == "__main__":
    simple_gantt()

