import pandas as pd


def gen_stat(df, p_hand='total', stats=['avg', 'obp', 'total_bases', 'runs_created', 'rc_per_game']):
    """Adds the specified stats to the passed through weighted DataFrame"""
    if 'avg' in stats:
        df['weighted_AVG'] = df['H_vs_' + p_hand] / df['AB_vs_' + p_hand]
    if 'obp' in stats:
        df['weighted_obp'] = ((df['H_vs_' + p_hand] + df['BB_vs_' + p_hand] + df['HBP_vs_' + p_hand]) /
                              (df['AB_vs_' + p_hand] + df['SF_vs_' + p_hand] + df['BB_vs_' + p_hand] + df[
                                  'HBP_vs_' + p_hand]))
    if 'total_bases' in stats:
        df['weighted_total_bases'] = df['1B_vs_' + p_hand] + (2 * df['2B_vs_' + p_hand]) + \
                                     (3 * df['3B_vs_' + p_hand]) + (4 * df['HR_vs_' + p_hand])
    if 'runs_created' in stats:
        df['weighted_runs_created'] = (((df['H_vs_' + p_hand] + df['BB_vs_' + p_hand] -
                                         df['CS_vs_' + p_hand] + df['HBP_vs_' + p_hand] -
                                         df['GDP_vs_' + p_hand]) * (
                                                df['weighted_total_bases'] +
                                                (0.26 * (df['BB_vs_' + p_hand] -
                                                         df['IBB_vs_' + p_hand] +
                                                         df['HBP_vs_' + p_hand])) +
                                                0.52 * (df['SH_vs_' + p_hand] +
                                                        df['SF_vs_' + p_hand] +
                                                        df['SB_vs_' + p_hand]))) /
                                       (df['AB_vs_' + p_hand] + df['BB_vs_' + p_hand] +
                                        df['HBP_vs_' + p_hand] + df['SH_vs_' + p_hand] +
                                        df['SF_vs_' + p_hand]))
    if 'rc_per_game' in stats:
        df['weighted_runs_created_per_game'] = df['weighted_runs_created'] / df['G_vs_' + p_hand]
    return df
