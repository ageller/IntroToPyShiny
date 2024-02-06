# Intro To Shiny for Python
Shiny lets you build interactive dashboards and websites without knowing HTML, CSS, or Javascript. Create tools for yourself, or share your data, analysis, and visualizations with the world through simple apps and interfaces. This workshops introduces Shiny for Python (yes Python!).  You will learn how to build and deploy a basic Shiny app, with multiple figures and a user interface containing widgets that control the figure content.

I originally developed some materials for this workshop in my [disasterShinyPy GitHub repo](https://github.com/ageller/disasterShinyPy).  You can also read about my initial experience with Python + Shiny on my blog post [here](https://sites.northwestern.edu/researchcomputing/2023/04/12/experimenting-with-shiny-for-python/).

In this workshop, we will build an app that is similar to [this version on shinyapps.io](https://ageller.shinyapps.io/disasterpy/).

Earthquake data come from the USGS and were downloaded [here](https://www.kaggle.com/datasets/thedevastator/uncovering-geophysical-insights-analyzing-usgs-e), and volcano data come The Simithsonian Institute and were downloaded from [here](https://www.kaggle.com/datasets/jessemostipak/volcano-eruptions).

You can access the presentation [on Google Slides here](https://docs.google.com/presentation/d/1XEwFZRhWh1zjKL4oQAqYKrUFbs1Ij8wT/edit?usp=sharing&ouid=100526071325620132362&rtpof=true&sd=true). 


## Running locally

If you want to run the examples locally, you can clone this repo and follow these steps:

1. I recommend creating a conda environment.  
    ```
    conda create --name shinyTest python shiny pandas matplotlib cartopy
    conda activate shinyTest
    ```

2. Withing the `examples/` directory run the app with 
    ```
    shiny run --reload example1_1.py
    ```

    (and replace `example1_1.py` with the file that you want to run)

3. Point your browser to http://127.0.0.1:8000/ to view your app.
