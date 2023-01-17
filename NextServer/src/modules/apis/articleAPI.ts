import { Article } from "../types"
import axios, { AxiosResponse } from 'axios'
import { currentTime } from '@/components/admin/utils'

export const article = {
    async join(payload: Article){
        try{
            const response : AxiosResponse<any, Article[]> =
            await axios.post(`http://localhost:8000/articles/write`, payload, {headers: {
                "Content-Type" : "application/json",
                Authorization: "JWT fefege...",
            }})
            if(response.data === "success"){
                alert(' 결과: API 내부 join 성공  '+ JSON.stringify(response.data))
            }else{
                alert(` 결과: ${JSON.stringify(response.data)}`)
            }
            
            return response
        }catch(err){
            console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
        }
    }
}