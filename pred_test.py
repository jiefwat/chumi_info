from mul_models_info import SkuDemodsPred
import pandas as pd
# import cx_Oracle
# cx_Oracle.init_oracle_c lient(lib_dir=r"/Users/kaka/Downloads/instantclient_18_1")

import time


def get_full_skulist(connection):
    sql_query = """  select 
                  HOSTPARTID 
          from nppbuf.t_dd_detail_ml where  historybegdate>=20230101
          group by HOSTPARTID
    """
    # 执行 SQL 查询，并按批次抽取数据
    query_chunks = pd.read_sql(sql_query, connection)
    # 遍历查询结果的每个批次，并将其合并为一个 DataFrame
    return query_chunks


def clear_table_in_oracle(connection):
    # 连接到Oracle数据库
    cursor = connection.cursor()
    query = "TRUNCATE TABLE nppbuf.T_DD_demand_detail_fstout"
    cursor.execute(query)


def get_full_counts(connection):
    sql_query = """  select 
                  count(*) 
          from nppbuf.t_dd_detail_ml where historybegdate>=20230101
    """
    # 执行 SQL 查询，并按批次抽取数据
    query_chunks = pd.read_sql(sql_query, connection)
    # 遍历查询结果的每个批次，并将其合并为一个 DataFrame
    return query_chunks


def get_data_from_oracle(connection,sku_list):

    sql_query = """  
         select *
      from nppbuf.t_dd_detail_ml 
      where HOSTPARTID  in {} and historybegdate>=20230101
    """.format(sku_list)
    # 执行 SQL 查询，并按批次抽取数据
    chunksize = 100000  # 每次查询返回的行数，你可以根据需要调整这个值
    query_chunks = pd.read_sql(sql_query, connection, chunksize=chunksize)
    # 遍历查询结果的每个批次，并将其合并为一个 DataFrame
    data = pd.DataFrame()
    for chunk in query_chunks:
        data = data.append(chunk)
    # 关闭数据库连接
    connection.close()
    # 输出合并后的 DataFrame
    return data


def main():
    ods = SkuDemodsPred()
    connection = ods.mysql_info()
    clear_table_in_oracle(connection)
    print('----预测结果表预测前清空----')
    full_counts = get_full_counts(connection)
    counts_info = float(full_counts['COUNT(*)'])
    print('样本总数：',counts_info)
    full_sku_list = get_full_skulist(connection)['HOSTPARTID'].tolist()
    num_info = 0
    for i in range(0, len(full_sku_list), 200):
        fst_time = time.time()
        connection = ods.mysql_info()
        new_sku_list = full_sku_list[i:i + 200]
        my_tuple = tuple(new_sku_list)
        data = get_data_from_oracle(connection,my_tuple)
        # print('处理样本数量：', data.shape)
        num_info+=data.shape[0]
        print('待完成数量：',counts_info -num_info)
        ods.main(data,'train')
        end_time =time.time()
        print('该批次耗时',(end_time-fst_time)/60 )

if __name__ == '__main__':
    fst_full_time = time.time()
    main()

    end_full_time = time.time()
    print('总耗时：',(end_full_time -fst_full_time)/60)

