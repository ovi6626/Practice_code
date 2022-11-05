# use from JupyterNotebook ( .ipynb ) and pandas
# import nullval as nv <-- use this alias

class null:

    # check null value
    # data is DataFrame, head is check from the order in which there are a lot of nullvalue
    def data_check(data=None, head=int):
        null_count = data.isnull().sum()
        null_count_ck = null_count.reset_index()
        null_count_ck.columns = ['collist', 'null']
        null_count_ck = null_count_ck.sort_values(by='null', ascending=False).head(head)
        return null_count_ck

    # remove data
    # data is DataFrame, top is columns you want to delete
    def data_remove(data=None, top=int):
        null_data = null.data_check(data, top)
        null_data = null_data['collist'].values
        print(data.shape)
        print('Delete data...')
        data = data.drop(null_data, axis=1)
        print(data.shape)
        if top != 1:
            print(top, 'columns has remove')
        else:
            print('1 columns have remove')
        return data
