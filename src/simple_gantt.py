# simple_gantt.py
# Author: cheesemeup

"""This script generates a very simple Gantt chart, based on the configuration in the runscript.

The intended resolution is in months, to provide a rough outline for work packages in multi-year projects
"""

import json
import matplotlib.patches as patches
import matplotlib.pyplot as plt

def simple_gantt():
    """Driver for creating a simple Gantt chart

    Reads a config file, which is generated by the runscript, and creates a Gantt chart based on the configuration
    """
    # get config
    config = get_config()

    # make chart
    make_chart(config)


def get_config() -> dict:
    """Get the config for the Gantt chart specified in the runscript

    Returns:
        config (dict): Configuration for the Gantt chart
    """
    # open file and read content
    # the config file location and name is hardcoded, as it is generated by the runscript
    with open('simple_gantt_config.cnf') as file:
        config_string = file.read()

    # convert from string representation of a dict to an actual dict for ease of use
    config = json.loads(config_string)

    # log
    print('config read')
    return config


def make_chart(config: dict):
    """Create and save the chart

    Args:
        config (dict): Configuration for the Gantt chart
    """
    # full duration of the project
    full_duration = max(max(config["work_packages"]))

    # open figure
    fig = plt.figure()

    # zoom based on the number of tasks and months
    ax = plt.gca()
    ax.set_xlim([0,full_duration])
    ax.set_ylim([0,len(config["work_packages"])+1])

    # title and axis labels
    plt.title(config["figure_title"])

    # create axis labels, note that order is inverted
    ytick_positions, ytick_labels = generate_yticks(len(config["work_packages"]))
    ax.set_yticks(ytick_positions, ytick_labels)
    xtick_position, xtick_label = generate_xticks(full_duration, config["temporal_resolution"])
    ax.set_xticks(xtick_position, xtick_label)


    # create boxes, note that the order is inverted, with WP 1 being at the top
    for i in range(len(config["work_packages"])):
        ax.add_patch(patches.Rectangle(
            [config["work_packages"][i][0],ytick_positions[i]-0.5],
            config["work_packages"][i][1]-config["work_packages"][i][0],
            1,
            color=config["box_color"]
        ))
###
    # save figure
    plt.show()
    plt.savefig(f"out/{config['figure_filename']}")
    plt.close()

    # log
    print(f"figure saved as out/{config['figure_filename']}")


def generate_yticks(n_work_packages: int) -> [list[float], list[str]]:
    """Generate the ytick locations and labels for the chart

    Args:
        n_work_packages (int): The number of work packages

    Returns:
        ytick_positions (list[float]): The y positions of the ticks
        ytick_labels (list[str]): The tick labels
    """
    ytick_positions, ytick_labels = [], []
    # for loop, reversing the order of work packages to have WP 1 at the top of the chart
    for i in range(n_work_packages):
        ytick_positions.append(n_work_packages-i)
        ytick_labels.append(f"WP {i+1}")

    # log
    print(f"ytick positions: {ytick_positions}")
    print(f"ytick labels: {ytick_labels}")

    return ytick_positions, ytick_labels

def generate_xticks(full_duration: int, temporal_resolution: int) -> [list[float], list[str]]:
    """Generate the xtick locations and labels for the chart

    Args:
        full_duration (int): Full duration of the project, in months
        temporal_resolution (int): The temporal resolution of the ticks

    Returns:
        xtick_positions (list[float]): The x positions of the ticks
        xtick_labels (list{str}): The tick labels
    """
    # initialize empty lists
    xtick_positions, xtick_labels = [], []

    # for loop to add tick information to lists
    for i in range(0,full_duration+1,temporal_resolution):
        xtick_positions.append(i)
        xtick_labels.append(f"{i}")

    # log
    print(f"xtick positions: {xtick_positions}")
    print(f"xtick labels: {xtick_labels}")

    return xtick_positions, xtick_labels


if __name__ == "__main__":
    simple_gantt()

