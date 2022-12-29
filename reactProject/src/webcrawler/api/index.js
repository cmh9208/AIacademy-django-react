// import axios from 'axios'
// const server = `http://localhost:8000`
// export const stroke = req => axios.get(`${server}/webcrawler/webcrawler`, req)

const server = `http://localhost:8000`



const dlearnService = {a}

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


async function a(){
    fetch(`${server}/webcrawler/webcrawler`)
    .then(handleResponse)
    .then(data => {
        alert('결과: '+JSON.stringify(data))
    })
    .catch((error) => {
        alert('error :::: '+error);
    });
} 


export default dlearnService