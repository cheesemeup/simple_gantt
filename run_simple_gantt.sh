# !/bin/bash
#
# run_simple_gantt.sh
# Author: cheesemeup
#
# runscript that contains the configuration for the simple_gantt script, and runs it

# configuration
cat << EOF > simple_gantt_config.cnf
{
    "work_packages":[[0,15],[15,27],[27,36]],
    "figure_title":"Project Timeline",
    "figure_filename":"timeline_gantt.png",
    "temporal_resolution":3
}
EOF

# run simple_gantt
python src/simple_gantt.py simple_gantt_config.cnf

