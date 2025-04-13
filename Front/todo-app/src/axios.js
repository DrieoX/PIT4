import axios from 'axios';

const api = axios.create({
  baseURL: 'https://pit4.onrender.com/',
  headers: {
    'Content-Type': 'application/json',
    // Include other headers if necessary, e.g., Authorization
  },
});

export default api;
