import matplotlib.pyplot as plt

def generate_pie_chart():
    lab = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=lab)
    plt.savefig('pie.png')
    plt.close()