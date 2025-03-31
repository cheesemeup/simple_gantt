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
    full_duration = max(max(config["task_timespans"]))

    # open figure with settings
    fig = plt.figure(figsize=(18,8))

    # zoom based on the number of tasks and months
    ax = plt.gca()
    ax.set_xlim([0,full_duration])
    ax.set_ylim([0.5,len(config["tasks"])+0.5])

    # title and axis labels
    plt.title(config["figure_title"], fontsize=24)
    plt.xlabel('Month', fontsize=24)

    # create axis labels, note that order is inverted
    ytick_positions, ytick_labels = generate_yticks(config["tasks"])
    ax.set_yticks(ytick_positions, ytick_labels, fontsize=24)
    xtick_position, xtick_label = generate_xticks(full_duration, config["temporal_resolution"])
    ax.set_xticks(xtick_position, xtick_label, fontsize=24)


    # create boxes, note that the order is inverted, with WP 1 being at the top
    for i in range(len(config["tasks"])):
        ax.add_patch(patches.Rectangle(
            [config["task_timespans"][i][0],ytick_positions[i]-0.5],
            config["task_timespans"][i][1]-config["task_timespans"][i][0],
            1,
            color=config["box_color"][i]
        ))

    # legend
    unique_colors = []
    for color in config["box_color"]:
        if not color in unique_colors:
            unique_colors.append(color)
    n_colors = len(unique_colors)
    for wp in range(n_colors):
        ax.add_patch(patches.Rectangle((-1,-1),0,0,color=unique_colors[wp],label=f"WP {wp+1}"))
    plt.legend(loc="upper right", fontsize=24, framealpha=1)

    # vertical lines
    for segment in range(0,full_duration,config["temporal_resolution"]):
        if segment%12 == 0:
            linestyle = '-'
            linewidth=3
        else:
            linestyle = '--'
            linewidth=1
        plt.plot([segment,segment],[0.5,len(config["tasks"])+0.5],linestyle=linestyle,linewidth=linewidth,c='k')

    # horizontal lines
    for task in range(len(config["tasks"])):
        plt.plot([0,full_duration],[task+0.5,task+0.5],c='k')


    # save figure
    fig.tight_layout()
    plt.show()
    fig.savefig(f"out/{config['figure_filename']}")
    plt.close()

    # log
    print(f"figure saved as out/{config['figure_filename']}")


def generate_yticks(tasks: list[str]) -> [list[float], list[str]]:
    """Generate the ytick locations and labels for the chart

    Args:
        tasks (list[str]): The list of tasks

    Returns:
        ytick_positions (list[float]): The y positions of the ticks
        ytick_labels (list[str]): The tick labels
    """
    ytick_positions, ytick_labels = [], []
    # for loop, reversing the order of tasks to have task 1 at the top of the chart
    for i in range(len(tasks)):
        ytick_positions.append(len(tasks)-i)
        ytick_labels.append(f"{tasks[i]}")

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

