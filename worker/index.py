from src.core.dataset import load_trips, load_vendor, update_payment
from src.core.plotter import plot_mean, plot_top_vendors, money_paid_trips, daily_tips
from src.models import queries
import time

print('Starting ETL.')

def main():

    print('starting trips loading.')
    load_trips(queries.table_trips, queries.table_trips_columns, queries.json_path)
    print('trips table loaded')

    print('starting vendor loading')
    load_vendor(queries.table_vendor_lookup, queries.table_vendor_lookup_columns, queries.vendor_path)
    print('vendor table loaded')

    print('starting update')
    update_payment(queries.table_trips, queries.payment_path)
    print('update ended')

    print('A distância média percorrida por viagens com no máximo 2 passageiros:')
    plot_mean(queries.avg_distance_2_passengers)

    print('Os 3 maiores vendors em quantidade total de dinheiro arrecadado são:')
    plot_top_vendors(queries.top_vendors)
    print('PNG gerado')

    print('Distribuição mensal, nos 4 anos, de corridas pagas em dinheiro:')
    money_paid_trips(queries.money_paid)
    print('PNG gerado')

    print('Quantidade de gorjetas por dia nos últimos 3 meses de 2012:')
    daily_tips(queries.tips_per_day)
    print('PNG gerado')

    return True

time.sleep(45)
main()