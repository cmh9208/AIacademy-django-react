// 

// import axios from 'axios'
const server = `http://localhost:8000`
// export const userLogin = req => axios.post(`${server}/samsung_report/samsung`, req)


// export const userLogin = req => axios.post(`http://localhost:8000/blog/auth/login`, req)

const samsungService = {
    sam
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
    
async function sam(){
    const res = await fetch(`${server}/samsung_report/samsung`)
    .then(handleResponse)
    .then(data => JSON.stringify(data))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
} 

export default samsungService

