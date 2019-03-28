
# coding: utf-8

# In[1]:


import folium
import pandas as pd
from folium import plugins
 
SF_COORDINATES = (37.76, -122.45)
crimedata = pd.read_csv('Police_Department_Incident_Reports__2018_to_Present.csv')
 
crimedata=crimedata.dropna(subset=['Latitude', 'Longitude'])
# for speed purposes
MAX_RECORDS = 20
  
# create empty map zoomed in on San Francisco
map = folium.Map(location=SF_COORDINATES, zoom_start=12)
 

# add a marker for every record in the filtered data, use a clustered view
#for each in crimedata[0:2000].iterrows():
 #   folium.CircleMarker(
  #      location = [each[1]['Latitude'],each[1]['Longitude']], 
   #     clustered_marker = True,fill=True).add_to(map)
    
locations = crimedata[0:30000][['Latitude', 'Longitude']].as_matrix()

# plot heatmap
map.add_children(plugins.HeatMap(locations, radius=7))

  
display(map)


# In[2]:


healthBuildings=pd.read_csv('Health_Care_Facilities.csv')


# In[3]:


businessdata = pd.read_csv('Registered_Business_Locations_-_San_Francisco.csv')
businessdata.shape
first10=businessdata['Street Address'][:10]


# In[ ]:





# In[4]:


businessdata.columns


# In[21]:


businessdata.columns

addresses=businessdata[['Street Address','City', 'State','Source Zipcode']][:5000]
addresses.head()
BusinessAddresses = addresses.to_csv (r'C:\Users\Nick Rezaee\Desktop\BusinessAddresses.csv')


# In[13]:


busin=pd.read_csv("BusinessAddresses.csv")


# In[7]:


busin.head()


# In[67]:


fake=pd.read_csv('Addresses.csv')
fake.head()


# In[55]:


realLocations=pd.read_csv("GeocodeResults (3).csv")
realLocations.shape


# In[58]:


neededData=businessdata[(businessdata['NAICS Code Description']=='Private Education and Health Services') & (businessdata['Business End Date'].isnull())]
neededData.head()


# In[56]:


businessdata['NAICS Code Description'].unique()


# In[50]:


NaN=businessdata['Business End Date'][0]
type(NaN)


# In[49]:


businessdata[businessdata['Business End Date']==NaN]

