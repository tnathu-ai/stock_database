def concat_all(folder_name):
    # csv files in the path
    # All files and directories ending with .txt with depth of 2 folders, ignoring names beginning with a dot:
    files = glob.glob("../../data/external/National Leagues/*" + "/*.csv")

    # defining an empty list to store
    # content
    data_frame = pd.DataFrame()
    content = []

    # checking all the csv files in the
    # specified path
    for filename in files:
        # reading content of csv file
        # content.append(filename)
        df = pd.read_csv(filename, index_col=None)
        content.append(df)

    # converting content to data frame
    df = pd.concat(content)

    # Only get needed columns
    df = df[['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'Referee', 'HS', 'AS',
             'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']]

    df.loc[:, 'season'] = folder_name

    # print out list of District types
    print(
        f'NUMBER OF DATE CATEGORIES: {df.Date.nunique()}; \n\nUNIQUE NAMES OF THE DATE CATEGORIES {df.Date.unique()}\n')

    print(f'The number of columns: {len(df.columns)}')
    print(f'The list of the {folder_name} final columns\' names is: {df.columns.to_list()}\n\n\n')
    return df




def concat_all(folder_name):
    # set the path of the external data from the third party source
    external_data_path = os.path.join(os.path.pardir, '', '..', 'data', 'external', 'National Leagues', folder_name)

    # csv files in the path
    files = glob.glob(external_data_path + "/*.csv")

    # defining an empty list to store
    # content
    data_frame = pd.DataFrame()
    content = []



    # checking all the csv files in the
    # specified path
    for filename in files:
        # reading content of csv file
        # content.append(filename)
        df = pd.read_csv(filename, index_col=None)
        content.append(df)

    # converting content to data frame
    df = pd.concat(content)

    # Only get needed columns
    df = df[['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'Referee', 'HS', 'AS',
             'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']]

    df.loc[:, 'season'] = folder_name

    # print out list of District types
    print(
        f'NUMBER OF DATE CATEGORIES: {df.Date.nunique()}; \n\nUNIQUE NAMES OF THE DATE CATEGORIES {df.Date.unique()}\n')

    print(f'The number of columns: {len(df.columns)}')
    print(f'The list of the {folder_name} final columns\' names is: {df.columns.to_list()}\n\n\n')
    return df




