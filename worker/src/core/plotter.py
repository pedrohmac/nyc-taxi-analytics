from src.services.postgres import create_connection
import matplotlib.pyplot as plt

def plot_mean(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return print(round(data[0][0], 2))


def plot_top_vendors(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    handler = {value[0]:round(value[1],2) for value in data}
    names = list(handler.keys())
    values = list(handler.values())

    width = 0.95
    fig, ax = plt.subplots()
    rects = ax.bar(names, values, width)
    ax.set_title('Os 3 maiores vendors em quantidade total de dinheiro arrecadado são:')

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height - .5,
                'R$ %d' % int(height),
                ha='center', va='bottom')
    ax.axes.get_yaxis().set_visible(False)
    
    return plt.savefig('./graphs/top_vendors.png')


def money_paid_trips(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    response = cursor.fetchall()

    handler = [list(value) for value in response]
    data = [str(value[0])[5:7] for value in handler]

    month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']

    value_list = []
    for month in month_list:
        value=0
        for record in data:
            if month == record:
                value+=1
        value_list.append(value)

    fig, ax = plt.subplots()
    rects = plt.bar(month_list, value_list, 1)
    ax.set_title('Distribuição mensal, nos 4 anos, de corridas pagas em dinheiro:')

    for idx, rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
                value_list[idx],
                ha='center', va='bottom', rotation=90)

    return plt.savefig('./graphs/money_paid_trips.png')


def daily_tips(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    response = cursor.fetchall()

    handler = [list(value) for value in response]


    date_list = []
    tips_list = []
    for i in handler:
        date_list.append(str(i[0])[5:])
        tips_list.append(round(i[1],2))

    fig, ax = plt.subplots()
    rects = plt.bar(date_list, tips_list, .9)
    fig.subplots_adjust(bottom=0.25)
    ax.set_title('Quantidade de gorjetas de cada dia, nos últimos 3 meses de 2012:')

    for idx, rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
                tips_list[idx],
                ha='center', va='bottom', rotation=90, color='white')

    plt.xticks(rotation=60)

    plt.savefig('./graphs/tips.png')

    return True