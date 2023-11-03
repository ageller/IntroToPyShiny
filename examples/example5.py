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
app_ui = ui.page_sidebar(

 
    # UI 
    ui.sidebar(
        ui.h2("Controls"),
        ui.input_checkbox_group(
            "toggle", "Show/Hide data", {"Earthquakes": "Earthquakes (blue)", "Volcanoes": "Volcanoes (red)"},
            selected = ["Earthquakes", "Volcanoes"]
        ),
        ui.panel_conditional(
            "input.toggle.includes('Earthquakes')",
            ui.br(),
            ui.h4("Earthquake inputs"),
            ui.input_radio_buttons(
                "eCol", "Attribute to plot:", {"mag": "Magnitude", "depth": "Depth (km)"}
            ),
            ui.input_slider(
                "eSize", "Size scale for map:", min=1, max=500, value=20, step=1
            ),
        ),

        ui.br(),
        ui.h4("Volcano inputs"),
        ui.input_radio_buttons(
            "vCol", "Attribute to plot:", {"elevation": "Elevation (m)", "population_within_100_km" : "Population within 100km"}
        ),
        ui.input_slider(
            "vSize", "Size scale for map:", min=1, max=500, value=20, step=1
        ),
        width = 300, bg = 'lightgray'
    ),

   # title
    ui.h1("Earthquakes and Volcanoes"),
    ui.p("Earthquakes are plotted in blue; the data come from the USGS (downloaded from ", ui.a("here", href = "https://www.kaggle.com/datasets/thedevastator/uncovering-geophysical-insights-analyzing-usgs-e"), ") and show all earthquakes from 2022.  Volcanoes are plotted in red; the data come from The Smithsonian Institute (downloaded from ", ui.a("here", href = "https://www.kaggle.com/datasets/jessemostipak/volcano-eruptions"), ") and show all recorded volcanoes."),


    # plots
    # scatter plot
    ui.card(
        ui.output_plot("evscatter")
    ),

    # 2 histograms
    ui.card(
        ui.row(
            ui.column(6, 
                ui.panel_conditional(
                    "input.toggle.includes('Earthquakes')",
                    ui.output_plot("ehist")
                ),
            ),
            ui.column(6, ui.output_plot("vhist")),
        ),
    )

)

        
# this section does the "heavy lifting"
def server(input, output, session):

    ecolor = [13/255., 106/255., 255/255.]
    vcolor = [255/255., 29/255., 13/255.]

    # create the two histogram using matplotlib
    @output
    @render.plot()
    def ehist():
        fig, ax = plt.subplots()
        ax.hist(edf[input.eCol()], bins = 25, color = ecolor)
        ax.set_ylabel('N')
        ax.set_xlabel(f'Earthquake {input.eCol()}')
        return fig
    
    @output
    @render.plot()
    def vhist():
        fig, ax = plt.subplots()
        ax.hist(vdf[input.vCol()], bins = 25, color = vcolor)
        ax.set_ylabel('N')
        ax.set_xlabel(f'Volcano {input.vCol()}')
        return fig  

    # create a scatter plot of longitude vs. latitute
    @output
    @render.plot()
    def evscatter():
        esz = input.eSize()*(edf[input.eCol()] - min(edf[input.eCol()]))/(max(edf[input.eCol()]) - min(edf[input.eCol()]))
        vsz = input.vSize()*(vdf[input.vCol()] - min(vdf[input.vCol()]))/(max(vdf[input.vCol()]) - min(vdf[input.vCol()]))
        fig, ax = plt.subplots()
        if ('Earthquakes' in input.toggle()): 
            ax.scatter(edf['longitude'], edf['latitude'], color = ecolor, s = esz, alpha = 0.25)
        ax.scatter(vdf['longitude'], vdf['latitude'], color = vcolor, s = vsz, alpha = 0.25)
        ax.set_ylabel('Longitude')
        ax.set_xlabel('Latitude')
        ax.set_xlim(-180, 180)
        ax.set_ylim(-90, 90)
        return fig  
    
# define the app    
app = App(app_ui, server)