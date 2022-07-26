import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))].copy()

def draw_line_plot():
    # Draw line plot
    sns.set(font_scale=2)
    sns.set_style("ticks")
    plt.rcParams["font.family"] = "dejavu sans"
    fig, ax = plt.subplots(figsize=(32, 10))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', y=1.01)
    sns.lineplot(data=df.value, ax=ax, color='crimson', linewidth=3)
    ax.set(xlabel='Date', ylabel='Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    months_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month
    df_bar.sort_values(['Years', 'Months'], inplace=True)

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15.14, 13.30))
    sns.barplot(x='Years', y='value', hue='Months', palette="tab10", edgecolor=None, data=df_bar, ax=ax, ci=None)
    ax.set(ylabel='Average Page Views')
    plt.legend(months_names, loc='upper left', title='Months')
    plt.xticks(rotation=90)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    sns.set(font_scale=1)
    fig, ax = plt.subplots(1, 2, figsize=(28.80, 10.80))
    sns.boxplot(x="year", y="value", data=df_box, ax=ax[0])
    sns.boxplot(x="month", y="value", data=df_box, ax=ax[1])

    ax[0].set(xlabel="Year", ylabel='Page Views')
    ax[1].set(xlabel="Month", ylabel='Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
