import axios from 'axios'
export const server = "http://127.0.0.1:8000/"
export const userLogin = req =>axios.get(`${server}users/login`, req)

export const userSinup = req =>axios.post(`${server}users/user`, req)


const BlogService = {
    blogPost
}

function handleResponse(response){ 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
    }
    
async function blogPost(){
    const res = await fetch(`${server}users/user`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
} 

export default BlogService

