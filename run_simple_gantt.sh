# !/bin/bash
#
# run_simple_gantt.sh
# Author: cheesemeup
#
# runscript that contains the configuration for the simple_gantt script, and runs it

# configuration
cat << EOF > simple_gantt_config.cnf
{
    "tasks":[
        "CNN training and testing groundwork",
        "Input parameter selection for WP 1 CNN",
        "Selection of 2D parameters",
	"Evaluation of WP 1 CNN",
	"CNN training using forecast data",
	"Input parameter adjustment for WP 2 CNN",
        "Evaluation of WP 2 CNN",
        "Operationalization of RI forecasting",
        "Evaluation of operational forecasts",
        "Publication for WP 1 CNN",
        "Publication for WP 2 CNN",
        "Publication of operational service"
        ],
    "task_timespans":[
        [0,6],
        [6,12],
        [9,12],
	[9,15],
	[15,21],
	[18,24],
	[21,27],
	[24,30],
	[30,36],
        [12,24],
	[24,36],
	[30,36]
	],
    "figure_title":"Project Timeline",
    "figure_filename":"timeline_gantt.png",
    "temporal_resolution":3,
    "box_color":[
	"blue",
	"blue",
	"blue",
	"blue",
	"orange",
	"orange",
	"orange",
	"green",
	"green",
	"blue",
	"orange",
	"green",
	"green",
	"green",
	"blue",
	"orange",
	"green"
	]
}
EOF

# run simple_gantt
python src/simple_gantt.py simple_gantt_config.cnf

