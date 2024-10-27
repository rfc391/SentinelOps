import React, { useEffect, useState } from 'react';
import mapboxgl from 'mapbox-gl';
import { io } from 'socket.io-client';

mapboxgl.accessToken = 'your_mapbox_access_token';

const Dashboard = () => {
  const [map, setMap] = useState(null);
  const socket = io('http://localhost:5000');

  useEffect(() => {
    const initializeMap = () => {
      const map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [-74.5, 40],
        zoom: 9
      });

      setMap(map);
    };

    initializeMap();

    socket.on('updateData', (data) => {
      // Handle real-time data on the map here
    });

  }, []);

  return <div id="map" style={{ height: '100vh' }} />;
};

export default Dashboard;
