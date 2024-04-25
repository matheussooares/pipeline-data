

def get_columns(data):
    return list(data[-1].keys())

def rename_columns(data, key_mapping):
    transf_datacsv = []
    for old_dict in data:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        transf_datacsv.append(dict_temp)
    return transf_datacsv

def data_join(dataA,dataB):
    datajoin = []
    datajoin.extend(dataA)
    datajoin.extend(dataB)
    return datajoin 

