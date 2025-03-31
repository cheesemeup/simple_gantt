# simple_gantt
VERY simple gantt chart creation tool

To create a Gantt chart, edit the configuration in the run_simple_gantt.sh file.
Editing the simple_gantt_config.cnf file directly will not work, as the runscript overwrites this file every time is it run.

The first key is a list of lists, where the inner lists consist of two elements. These two elements are the initial and final
month of an individual task, where every task requires such an inner list. In the chart, they will be labeled as WP1, WP2, WP3, etc.
The second key is the title that will be displayed at the top of the figure.
The third key is the file name, with the appropriate file format ending.
The fourth key is the temporal resolution of the time axis ticks, in full months.

To generate the chart from this configuration, run the run_simple_gantt.sh script.
