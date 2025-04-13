// src/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://pit4.onrender.com/api/todos',
  headers: {
    'Content-Type': 'application/json',
    // Include other headers if necessary, e.g., Authorization
  },
});

export default api;
