// 

import axios from 'axios'
const server = `http://localhost:8000`

export const userLogin = req => axios.post(`${server}/users/login`, req)


// export const userLogin = req => axios.post(`http://localhost:8000/blog/auth/login`, req)

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
    const res = await fetch(`${server}/users/signup`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
} 

export default BlogService