import { PayloadAction } from "@reduxjs/toolkit"
import { call, delay, put, takeLatest, takeLeading } from "redux-saga/effects"
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
            window.location.href = '/user/login'
        }catch(error){
            put(userAction.joinFailure(error))
        }
    })
}
/**
export function* watchLogin(){
    yield takeLatest(loginRequest, (action: {payload: User}) => {
        
        try{
            const response: any = user.login(action.payload)
            alert(`watch login성공 ${JSON.stringify(response.data)} `)
            put(loginSuccess({data: response.data}))
            window.location.href = '/'
        }catch(error){
            put(userAction.joinFailure(error))
        }
    })
}
 */
export interface UserLoginInput{ email: string, password: string }
function* login(action: {payload: UserLoginInput}){
    const {loginSuccess, loginFailure} = userAction
    const param = action.payload
    try{
        alert(`3 사가 내부 : ${JSON.stringify(param)}` )
        const response: User = yield call(user.login, param)
        yield put(loginSuccess(response))
        window.location.href = ('/loginHome')
    }catch(error){
        put(userAction.loginFailure(error))
    }
}
function* logout(action: {payload: UserLoginInput}){
    const {logoutSuccess, logoutFailure} = userAction
    const param = action.payload
    try{
        alert(`삭제하고자 하는 토큰 ${param}}`)
        const response: User = yield call(user.logout, param)
        alert(`로그아웃 결과 ${response}}`)
        yield put(logoutSuccess())
        window.location.href = ('/')
    }catch(error:any){
        put(userAction.logoutFailure(error))
    }
}

export function* watchLogin(){
    const {loginRequest} = userAction
    yield takeLeading(loginRequest, login)
}
export function* watchLogout(){
    const {logoutRequest} = userAction
    yield takeLeading(logoutRequest, logout)
}