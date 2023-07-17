# Li-Ion-Visualizer
UTK Li-ion visualizer tool

Originally written in a Tkinter GUI, the platform has been moved to Plotly in order to run in a web browser as well as user interaction with the underlying database.

## Build Status
Main creates a JSON file which is used to design an html webpage.
html files can be edited and adjusted to reflect design choices. Currently, index.html holds what is called an iframe, which determines the interaction behavior, while chart.html is the webpage itself.

Issues/further action:
Create area below the chart which displays a link when the user hovers over a data point on the plot
 
 ## Dependencies
 Note: By running the executable file, your computer should not require python to be installed, nor any dependencies required when running it locally.
 
 In order to run the main.py script, it is recommended that you are running python3 and all dependencies can be installed with pip.
  - The Interface was written using pandas and plotly.
  - Requires matplotlib & mplcursors library.

## Argument for Plotly
    - charts are more aesthetically pleasing in comparison to bokeh
    - inherent 3D plotting capability & support
    - hover over point shows data associated with the point
    - plotly supports hover callback funtions so link area below chart may be straight forward? JS might be needed for this which I don't have experience in. See https://dash.plotly.com/vtk/click-hover
    - plot area is customizable. See https://plotly.com/python/3d-scatter-plots/ and https://plotly.com/python-api-reference/generated/plotly.express.scatter_3d
    - larger community with more support/documentation
    - plotly runs on pandas and therefore can handle big data in the same manner - can work with R.
    - Tom already has a simple model working in a web browser using plotly
    - simple code & easy to learn
    - extensive debug layer on both python & html side
    
## Concerns for Plotly
    - Written in python & therefore difficult to tell if it will have all the desirable customization readily available for editing, still more likely than Bokeh.
    - Data management is dealt with primarily through pandas and does not have any inherent data structures or capabilty. (Pandas will likely be more than sufficient for this project)
    - Potentially difficult for user-interaction with the database

## Argument for bokeh
    - easy to use functions
    - supports big data with pandas - can work with R bindings
    - inherent data structe "ColumnDataFrame" which has capabilities that can sometimes be favorable over pandas dataframes - not sure if any of these additional capabilities is applicable for the Li-Ion Visualizer project
    - simple code & easy to learn


## Concerns for bokeh
    - No inherent 3D plotting, only provided examples
    - Less aesthetically pleasing compared to plotly
    - Smaller dev team, more focused capability, less support/updates
    - interaction capabilities will have to be determined while developing
    - More crude than plotly - but may have more powerful interaction capability

## Conclusion: Plotly or Bokeh

Plotly and Bokeh essentially serve the same purpose. Although they each have their respective implementations, the respective softwares are both written in Python & most of the data manipulation is dealt with the Pandas library. Bokeh has some inherent data management capabilities that can sometimes come in handy over Pandas dataframes. Due to both the frameworks being written in Python, it is tough at this moment in time to determine the ability to change some attributes to reflect desired design choices. 

All this being said, I believe that it is in the EESCL's best interest to continue pursuing Plotly. Due to the work Tom has already completed, there is a working model with most of the interactivity already implemented. Zoom, pinch, rotate & details on mouse hover are implemented and working within a web-browser. 

It would be necessary, on top of learning Bokeh functions and conventions, to translate all the current plotly model to bokeh. In addition, Bokeh may not have the desired interactivity regardless. If it has not already been done in Bokeh, or well defined in documentation, it is highly likely that the desired attribute will not be implemented in the model. On the other hand, with a community as large as plotly, it is highly likely that someone has attempted to perform a comparable task, with or without inherent plotly functions. With that said, it is typically held that Bokeh has more user-interactivity built into the framework compared to Plotly, but that they BOTH lack in this area.

For more in-depth information, refer to this article written on the comparison of the two Python libraries for data visualization applications. 

```
https://pauliacomi.com/2020/06/07/plotly-v-bokeh.html
```
  
