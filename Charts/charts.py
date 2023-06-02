import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
