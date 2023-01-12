import { PayloadAction } from "@reduxjs/toolkit"
import { call, delay, put, takeLatest } from "redux-saga/effects"
import { string } from 'yup'
import userActions from '@/modules/users'
import { currentTime } from "@/components/admin/utils"
import { userJoinApi } from "@/apis/userApi"
// api 

interface UserJoinType{
    type: string,
    payload: {
        user_email: string, password: string, user_name: string
    }
}
interface UserJoinSuccessType{
    type: string,
    payload: {
        username: string
    }
}
function* join(user: UserJoinType){
    try{
        console.log(` ${currentTime} : userSaga 내부에서 FastAPI에 넘기는 값 ${JSON.stringify(user)} `)
        //const response : UserJoinSuccessType = yield userJoinApi(user.payload)
        //console.log(` ${currentTime} : userSaga join 성공 ${JSON.stringify(response)} `)
    }catch(error){
        console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
    }
}
export function* watchJoin(){
    yield takeLatest(userActions.actions.joinRequest, join)
}