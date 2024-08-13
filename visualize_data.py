import pygal #needed for visualization
from matplotlib import pyplot as plt #needed for plotting
import csv #needed to work with csv

# Earthquake data visualization with Pygal
places = ['Hyuganada Sea, Japan', 'NW of Grapevine, CA', 'SW of Lamont, CA', 'E of Barcelona, Phillipines']
mags = [7.1, 4.44, 5.22, 6.3]

quakehist = pygal.Bar() #create visualization
quakehist.add('', mags) #add values for quake magnitudes

#label axes and add title
quakehist.title = "Significant Earthquakes in the Past 7 Days"
quakehist.x_labels = places
quakehist.x_title = "Location"
quakehist.y_title = "Magnitude (Richter Scale)"

quakehist.render_to_file('nm_quakes_week.svg') #create file in current directory

# Fire data visualization with Matplotlib
firefile = 'world_fires_1_day.csv' #set filename for file

latitude = []
longitude = []

with open(firefile) as f: #make a file object
    fires = csv.reader(f) #fires will read through the file
    header = next(fires) #grabs the first line as header without fire data

    for row in fires:
        latitude.append(float(row[0])) #store latitude as float
        longitude.append(float(row[1])) #store longitude as float

#labels and axis scale
plt.title('Worldwide Fire Data (Last 24 Hours)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis([-180.0, 180.0, -90.0, 90.0])

#plot fires in orange
plt.scatter(longitude, latitude, c='orange', linewidth=0, edgecolors='none', s=5)
plt.show()
