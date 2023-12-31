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

    # plots
    ui.row(
        ui.column(6, ui.output_plot("ehist")),
    )
)

        
# this section does the "heavy lifting"
def server(input, output, session):

    # create the two histogram using matplotlib
    @output
    @render.plot()
    def ehist():
        col = 'mag'
        fig, ax = plt.subplots()
        ax.hist(edf[col], bins = 25, color = [13/255., 106/255., 255/255.])
        ax.set_ylabel('N')
        ax.set_xlabel(f'Earthquake {col}')
        return fig
    

# define the app    
app = App(app_ui, server)