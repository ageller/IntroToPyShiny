import pandas as pd
from shiny import App, render, ui
import matplotlib.pyplot as plt

'''
read in the data
'''
# Earthquakes : https://www.kaggle.com/datasets/thedevastator/uncovering-geophysical-insights-analyzing-usgs-e
edf = pd.read_csv('../data/usgs_main.csv')

# Volcanoes : https://www.kaggle.com/datasets/jessemostipak/volcano-eruptions
vdf = pd.read_csv('../data/volcano.csv')

'''
The Shiny app

working from examples here https://shinylive.io/py/examples/
'''

# this section defines the layout
app_ui = ui.page_fluid(

    # could include a title and description here (will do that later)

    # UI can be included here (will do that later)

    # plots, 2 histograms
    ui.row(
        ui.column(6, ui.output_plot("ehist")),
        ui.column(6, ui.output_plot("vhist")),
    )
)

        
# this section does the "heavy lifting"
def server(input, output, session):

    # create the two histogram using matplotlib
    @output
    @render.plot()
    def ehist():
        col = 'depth'
        fig, ax = plt.subplots()
        ax.hist(edf[col], bins = 25, color = [13/255., 106/255., 255/255.])
        ax.set_ylabel('N')
        ax.set_xlabel(f'Earthquake {col}')
        return fig
    
    @output
    @render.plot()
    def vhist():
        col = 'population_within_100_km'
        fig, ax = plt.subplots()
        ax.hist(vdf[col], bins = 25, color = [255/255., 29/255., 13/255.])
        ax.set_ylabel('N')
        ax.set_xlabel(f'Volcano {col}')
        return fig  

# define the app    
app = App(app_ui, server)