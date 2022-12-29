import axios from 'axios'
const server = `http://localhost:8000`
export const fakeFaces = req => axios.get(`${server}/mplex/movies/fake-faces`, req)