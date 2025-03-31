# simple_gantt
VERY simple gantt chart creation tool

To create a Gantt chart, edit the configuration in the run_simple_gantt.sh file.
Editing the simple_gantt_config.cnf file directly will not work, as the runscript overwrites this file every time is it run.

The tasks key is a list of strings denoting the individual tasks.
The task_timespans key is a list of lists, with each inner list consisting of two integers, which denote the beginning and
end month of a task.
The figure_title key is the title displayed at the top of the chart
The figure_filename key is the file name of the saved figure, with the appropriate file format suffix.
The temporal resolution key is the temporal resolution of the chart time axis ticks, in months.
The box_color key is the acolor of the bar for each task. These colors are used to detect work packages, which are then
added in a legend. All tasks of one color are assumed to be one work package.

To generate the chart from this configuration, run the run_simple_gantt.sh script.
