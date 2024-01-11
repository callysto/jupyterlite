def get_data(season, season_type):
    """
    Return the data.

    Returns:
        list: The data.
    """
    if season == '1997-98' and season_type == 'Playoffs':
        import pandas as pd
        data = pd.read_csv('data/playoffs_1998.csv')
        return data
    else:
        return "Check that the season is '1997-98' and the season type is 'Playoffs'"