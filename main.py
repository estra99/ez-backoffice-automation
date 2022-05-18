from prepare_data import *

def get_sv_selling():
    df_sv = get_sv()
    df_orders = get_orders()
    list_sv_ids_selling = df_orders['Id_Vendedor'].unique().tolist()
    df_sv_selling = df_sv.loc[df_sv['fields.cedula'].isin(list_sv_ids_selling)]
    return df_sv_selling


def get_num_sales_sv():
    df_orders = get_orders()
    df_num_sales_per_sv = df_orders.groupby(['Id_Vendedor'])['Id_Vendedor'].count()
    return df_num_sales_per_sv


def main():
    sv_active = get_sv_selling()
    num_sales_sv = get_num_sales_sv()
    print("Los vendedores que han realizado ventas son: \n")
    print(sv_active)
    print("\nLa cantidad de ventas por vendedores:\n")
    print(num_sales_sv)
    
main()
    
    



