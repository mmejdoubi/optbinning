"""
Scorecard information.
"""

# Guillermo Navas-Palencia <g.navas.palencia@gmail.com>
# Copyright (C) 2020

from ..binning.binning_information import print_header
from ..binning.binning_information import print_optional_parameters


scorecard_default_options = {
    "target": "",
    "binning_process": None,
    "estimator": None,
    "scaling_method": None,
    "scaling_method_params": None,
    "intercept_based": False,
    "reverse_scorecard": False,
    "rounding": False,
    "verbose": False
}


def print_main_info(n_records, n_variables, time_total):
    cpu_time = round(time_total, 4)
    print("  Number of records   : {}".format(n_records))
    print("  Number of variables : {}".format(n_variables))
    print("  Time                : {:<7.4f} sec\n".format(cpu_time))


def print_scorecard_statistics(n_records, n_variables, target_dtype,
                               n_numerical, n_categorical, n_selected,
                               time_total, time_binning_process,
                               time_estimator, time_build_scorecard,
                               time_rounding):

    stats = (
        "  Statistics\n"
        "    Number of records             {:>10}\n"
        "    Number of variables           {:>10}\n"
        "    Target type                   {:>10}\n\n"
        "    Number of numerical           {:>10}\n"
        "    Number of categorical         {:>10}\n"
        "    Number of selected            {:>10}\n"
        ).format(n_records, n_variables, target_dtype, n_numerical,
                 n_categorical, n_selected)

    print(stats)

    p_binning_process = time_binning_process / time_total
    p_estimator = time_estimator / time_total
    p_build_scorecard = time_build_scorecard / time_total
    p_rounding = time_rounding / time_build_scorecard

    time_stats = (
        "  Timing\n"
        "    Total time            {:>18.2f} sec\n"
        "    Binning process       {:>18.2f} sec   ({:>7.2%})\n"
        "    Estimator             {:>18.2f} sec   ({:>7.2%})\n"
        "    Build scorecard       {:>18.2f} sec   ({:>7.2%})\n"
        "      rounding            {:>18.2f} sec   ({:>7.2%})\n"
        ).format(time_total, time_binning_process, p_binning_process,
                 time_estimator, p_estimator, time_build_scorecard,
                 p_build_scorecard, time_rounding, p_rounding)

    print(time_stats)


def print_scorecard_information(print_level, n_records, n_variables,
                                target_dtype, n_numerical, n_categorical,
                                n_selected, time_total, time_binning_process,
                                time_estimator, time_build_scorecard,
                                time_rounding, dict_user_options):
    print_header()

    if print_level == 2:
        dict_default_options = scorecard_default_options
        print_optional_parameters(dict_default_options, dict_user_options)

    if print_level == 0:
        print_main_info(n_records, n_variables, time_total)
    elif print_level >= 1:
        print_scorecard_statistics(n_records, n_variables, target_dtype,
                                   n_numerical, n_categorical, n_selected,
                                   time_total, time_binning_process,
                                   time_estimator, time_build_scorecard,
                                   time_rounding)
