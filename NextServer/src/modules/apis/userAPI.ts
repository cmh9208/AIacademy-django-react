import axios, { AxiosResponse } from 'axios'
import {context} from '@/components/admin/enums'
import { currentTime } from '@/components/admin/utils'
import { User } from '@/modules/types'
import { author, client } from "@/modules/controllers"

export const user = {
    async join(payload: User){
            try{
                const response : AxiosResponse<any, User[]> =
                await axios.post(`http://localhost:8000/users/register`, payload, {headers: {
                    "Content-Type" : "application/json",
                    Authorization: "JWT fefege...",
                }})
                if(response.data === "success"){
                    alert(' 결과: API 내부 join 성공  '+ JSON.stringify(response.data))
                }else{
                    alert(` 결과: ${response.data.msg}  `)
                }
                return response
            }catch(err){
                console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
            }
        },
    async login(payload: User){
        try{
            const response : AxiosResponse<any, User[]> =
            await author.post('http://localhost:8000/users/login', payload)
            alert(`4 API payload is ${JSON.stringify(response.data)}`)
            localStorage.clear()
            localStorage.setItem("session", JSON.stringify(response.data))
            return response.data
        }catch(err){
            return err;
        }
    },
    async logout(){
        try{
            await client.post('/users/logout')
        } catch(err){
            console.log(err)
            return err;
        }
    },
    async userInfo(){
        try{
            const response : AxiosResponse = await client.get(`/users/join`)
            return response.data
        } catch(err) {
            console.log(err)
            return err
        }
    }
    
}