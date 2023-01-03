
export const server = "http://127.0.0.1:8000/"
export const dlearn = "korean/"

const naverMovieReviewService = {classifyPositiveAboutReview}

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
async function classifyPositiveAboutReview(review){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(review)
    }
    const url = `${server}${dlearn}korean`
    const res = await fetch(url, requestOption)
    
    .then(handleResponse)
    .then(data => (JSON.stringify(data)))
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
}
export default naverMovieReviewService