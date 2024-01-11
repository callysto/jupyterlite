def cleaning(df):
    """
    Cleans the data.
    """
    import pandas as pd
    import json
    def make_dict(the_string):    
        a_dict = {}
        split_list = the_string.replace('{','').replace('}','').split('":')
        key = split_list[0].replace('"','')
        for item in split_list[1:]:
            item = item.replace('"','')
            split_by_commas = item.split(',')
            if len(split_by_commas) > 2:
                key = split_by_commas[-1]
            else:
                value = split_by_commas[0]
                a_dict[key] = value
            try:
                key = split_by_commas[-1]
            except:
                a_dict[key] = value
                print('done')
        return a_dict

    for_new_df = []
    for row in df['_raw']:
        try:
            j = json.loads(row)    
        except:
            j = make_dict(row)
        for_new_df.append(j)
        
    data = pd.DataFrame(for_new_df)
    return data