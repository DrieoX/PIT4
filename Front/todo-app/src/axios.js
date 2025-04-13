// src/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://your-backend-domain.com/api/', // Replace with your FastAPI backend URL
  headers: {
    'Content-Type': 'application/json',
    // Include other headers if necessary, e.g., Authorization
  },
});

export default api;
