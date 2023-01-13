import { PayloadAction } from "@reduxjs/toolkit"
import { call, delay, put, takeLatest } from "redux-saga/effects"
import { joinRequest, joinSuccess, loginRequest, loginSuccess,
    userAction } from '@/modules/slices';
import { User } from '@/modules/types';
// import { user } from '@/modules/controllers';
import { user } from '@/modules/controllers';
// api 

export function* watchJoin(){
    yield takeLatest(joinRequest, (action: {payload: User}) => {
        
        try{
            const response: any = user.join(action.payload)
            put(joinSuccess(response.payload))
            window.location.href = '/'
        }catch(error){
            put(userAction.joinFailure(error))
        }
    })
}
export function* watchLogin(){
    yield takeLatest(loginRequest, (action: {payload: User}) => {
        
        try{
            const response: any = user.login(action.payload)
            // put(loginSuccess(response.data))
            window.location.href = '/loginHome'
        }catch(error){
            put(userAction.joinFailure(error))
        }
    })
}

