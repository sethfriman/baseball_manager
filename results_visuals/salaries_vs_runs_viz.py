#IMPORTS
import pandas as pd
import datetime
from scipy import stats
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
sns.set(font_scale=1)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold


#abbreviations of all the teams
abv = ['ARI', 'ATL', 'BAL', 'BOS', 'CHW', 'CHC', 'CIN', 'CLE', 'COL', 'DET', 'HOU', 'KCR', 'LAA', 'LAD',
                      'MIA', 'MIL', 'MIN', 'NYY', 'NYM', 'OAK', 'PHI', 'PIT', 'SDP', 'SFG', 'SEA', 'STL', 'TBR', 'TEX',
                      'TOR', 'WSN']

# reading necessary data into dataframes
standings_df = pd.read_csv('../data_directory/standings_2021.csv')
stats_df = pd.read_csv('../data_directory/FanGraphs_total.csv')
salaries_df = pd.read_csv('../data_directory/salaries_21.csv')

stats_df['Date'] = pd.to_datetime(stats_df['Date'], format="%Y/%m/%d")
# only including 2021 stats
stats_2021 = stats_df[stats_df['Date'] > datetime.datetime(2021,1,1)]

#runs created metric for each game
stats_2021['total_bases'] = stats_2021['1B'] + (2 * stats_2021['2B']) + \
                                 (3 * stats_2021['3B']) + (4 * stats_2021['HR'])
stats_2021['Runs Created'] = (((stats_2021['H'] + stats_2021['BB'] -
                                     stats_2021['CS'] + stats_2021['HBP'] -
                                     stats_2021['GDP']) * (
                                            stats_2021['total_bases'] +
                                            (0.26 * (stats_2021['BB'] -
                                                     stats_2021['IBB'] +
                                                     stats_2021['HBP'])) +
                                            0.52 * (stats_2021['SH'] +
                                                    stats_2021['SF'] +
                                                    stats_2021['SB']))) /
                                   (stats_2021['AB'] + stats_2021['BB'] +
                                    stats_2021['HBP'] + stats_2021['SH'] +
                                    stats_2021['SF']))


def get_salary_vs_rc(list_teams):
  """ Sums up every team's runs created; prints and plots linear, quadratic, and exponential regressions models to depict a relationship between runs created and 
  team salary """
    list_salary = []
    list_rc = []
    df = pd.DataFrame()

    for i in list_teams:
        team_df = standings_df[standings_df['Tm'] == i]
        team_df = team_df.reset_index()
        team_salary = salaries_df['Payroll']
        team_stats_df = stats_2021[stats_2021['Tm'] == i]
        total_rc = team_stats_df['Runs Created'].sum()
        list_salary.append(team_salary)
        list_rc.append(total_rc)
    dict_wins = {'ABV': abv, 'Payroll': team_salary, 'rc': list_rc}
    df = pd.DataFrame(dict_wins)
    print(df)
    print('Correlation =', stats.pearsonr(df.Payroll, df.rc))
##########################
#PRINTING LINEAR REGRESSION
    # define x and y
    x_label = 'rc'
    y_feat = 'Payroll'

    # initialize linear regression object
    reg = LinearRegression()

    x = df.loc[:, x_label].values
    y = df.loc[:, y_feat].values
    # reshape x
    x = x.reshape(-1, 1)

    reg.fit(x, y)

    y_pred = reg.predict(x)

    model_string = y_feat + f'={reg.intercept_:.2f}'
    model_string += f'+ {reg.coef_[0]:.2f} {x_label}'

    # initialize y pred, stores predictions of y
    y_pred = np.empty_like(y)

    # initialize linear regression object
    reg = LinearRegression()

    n_splits = 10

    kfold = KFold(n_splits=n_splits)

    for train_idx, test_idx in kfold.split(x, y):
        # get training data
        x_train = x[train_idx, :]
        y_train = y[train_idx]

        # get test data
        x_test = x[test_idx, :]

        reg = reg.fit(x_train, y_train)

        y_pred[test_idx] = reg.predict(x_test)

    # cross validated r2
    r2_linear_score = r2_score(y_true=y, y_pred=y_pred)

    print("linear model:")
    print(model_string)
    print(f'r2 = {r2_linear_score:.5}')
###########################
#PRINTING EXPONENTIAL REGRESSION

    # initialize linear regression object
    reg = LinearRegression()

    # exponential regression
    reg.fit(x, np.log(y))

    # predict y
    y_pred = np.exp(reg.predict(x))

    a0 = reg.intercept_
    a1 = reg.coef_[0]
    alpha = np.exp(a0)

    # create string for model
    model_string = f'{y_feat} = {alpha:.2f} e^({a1:.5f} {x_label})'

    y_pred = np.empty_like(y)

    reg = LinearRegression()

    n_splits = 10

    # initialize kfold
    kfold = KFold(n_splits=n_splits)

    for train_idx, test_idx in kfold.split(x, y):
        # training data
        x_train = x[train_idx, :]
        y_train = y[train_idx]

        # test data
        x_test = x[test_idx, :]

        reg = reg.fit(x_train, np.log(y_train))

        y_pred[test_idx] = np.exp(reg.predict(x_test))

    # cross validated r2
    r2 = r2_score(y_true=y, y_pred=y_pred)

    # print exponential model
    print('Exponential model:')

    # print actual mode
    print(model_string)
    # print r2
    print(f'r2 = {r2:.5}')

###############################
#PRINTING QUADRATIC REGRESSION
    # 2nd degree polynomial
    degree = 2

    poly = PolynomialFeatures(degree=degree)
    x_poly = poly.fit_transform(x)

    # initialize linear regression object
    # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    # this is where i learned about fit_intercept
    reg = LinearRegression(fit_intercept=False)

    # polynomial regression
    reg.fit(x_poly, y)

    y_pred = reg.predict(x_poly)

    coef_pred = reg.coef_

    # create string for model
    str_monomial = []
    for deg, coef in enumerate(coef_pred):
        if coef == 0 and include_zero == False:
            continue
        str_monomial.append(f'{coef:+.5f} {x_label}^{deg:d}')

        # handle case of all zero coef
        if len(str_monomial):
            poly_string = ' '.join(str_monomial)
        else:
            poly_string = '0'

    model_string = f'{y_feat} = {poly_string}'

    poly = PolynomialFeatures(degree=deg)
    x_poly = poly.fit_transform(x)

    # initialize y_pred, stores predictions of y
    y_pred = np.empty_like(y)

    # linear regression object
    reg = LinearRegression(fit_intercept=False)

    n_splits = 10

    # initialize kfold
    kfold = KFold(n_splits=n_splits)

    for train_idx, test_idx in kfold.split(x_poly, y):
        # training data
        x_train = x_poly[train_idx, :]
        y_train = y[train_idx]

        # test data
        x_test = x_poly[test_idx, :]

        reg.fit(x_train, y_train)

        # estimate on test data
        y_pred[test_idx] = reg.predict(x_test)

    # r2
    r2_poly_score = r2_score(y_true=y, y_pred=y_pred)
    # quadratic model
    print('Quadratic model:')
    # print actual model
    print(model_string)
    # create and reshape new set of x data

#################
#PLOTTING
    x_plot_model = np.linspace(x.min(), x.max(), 101)
    x_plot_model = x_plot_model.reshape(-1, 1)
    # repredict y_pred for each model using x_plot

    # initialize linear regression object (for linear plot)
    reg_linear = LinearRegression()

    reg_linear.fit(x, y)

    y_linear = reg_linear.predict(x_plot_model)

    reg_exponential = LinearRegression()
    # fit regression as exponential
    reg_exponential.fit(x, np.log(y))
    # use regression model to predict y
    y_exponential = np.exp(reg_exponential.predict(x_plot_model))

    # Initialize linear regression object (for quadratic plot)
    reg_polynomial = LinearRegression(fit_intercept=False)
    # fit regression as polynomial
    reg_polynomial.fit(x, y)
    # use regression model to predict y
    y_polynomial = reg_polynomial.predict(x_plot_model)

    colormap = np.array(['r', 'g', 'b'])

    # define labels for x and y
    x_plot_label = 'Runs Created'
    y_plot_label = 'Total Team Salary (hundred million USD)'

    title = 'Total Team Runs Created Vs. Team Salary 2021'

    colors = {'ARI': 'black', 'ATL': 'dimgrey', 'BAL': 'rosybrown', 'BOS': 'maroon', 'CHW':'tomato', 'CHC': 'saddlebrown', 'CIN':'darkorange',
              'CLE': 'darkgoldenrod', 'COL': 'olive', 'DET': 'darkolivegreen', 'HOU':'lawngreen', 'KCR': 'paleturquoise', 'LAA':'lightseagreen', 'LAD': 'cyan',
              'MIA': 'deepskyblue', 'MIL': 'dodgerblue', 'MIN': 'crimson','NYY': 'peachpuff', 'NYM': 'brown', 'OAK': 'rebeccapurple',
              'PHI': 'indigo', 'PIT':'magenta', 'SDP':'midnightblue', 'SFG':'darkgoldenrod', 'SEA':'rosybrown','STL': 'peru', 'TBR': 'lime', 'TEX': 'royalblue',
              'TOR': 'indianred', 'WSN':'palevioletred'}



    # create scatter plot of x and y (area and price)
    plt.scatter(x, y, alpha=0.75, label='Team', c=df['ABV'].apply(lambda x: colors[x]))

    # linear model plot
    plt.plot(x_plot_model, y_linear, color='green', label=f'linear (r2 = {r2_linear_score:.2f})', marker="o", linewidth=0.5,  markersize=1.5)

    # exponential model plot
    plt.plot(x_plot_model, y_exponential, color='red', label=f'exponential (r2 = {r2:.2f})', marker='_', linewidth=0.5, markersize=1.5)

    # quadratic model plot
    plt.plot(x_plot_model, y_polynomial, color='blue', label=f'quadratic (r2 = {r2_poly_score:.2f})')

    #Adding labels on top of specified teams
    plt.annotate("LAD", (1289.688857, 174661524))
    plt.annotate("ATL", (1279.613000, 106964415.0))
    plt.annotate("HOU", (1310.290000, 147127725.0))


    # creating a dictionary
    font = {'size': 10}

    # using rc function
    plt.rc('font', **font)
    # labels
    plt.xlabel(x_plot_label)
    plt.ylabel(y_plot_label)
    plt.suptitle(title)
    # legend
    plt.legend()
    print('Correlation =', stats.pearsonr(df.Payroll, df.rc))
    # size of plot
    plt.gcf().set_size_inches(7,7)
    plt.show()
get_salary_vs_rc(abv)
