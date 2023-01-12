import { createSlice, PayloadAction } from "@reduxjs/toolkit"
export interface IUserType{
    user_id : string
    user_email : string
    password : string
    user_name : string
    phone : string
    birth : string
    address : string
    job : string
    user_interests : string
    token : string
    create_at: string
    updated_at: string
}
export interface IUserState{
    data: IUserType[]
    status: 'idle' | 'loading' | 'failed'
}
const initialState: IUserState = {
    data: [],
    status: 'idle'
}
const userSlice = createSlice({
    name: 'userSlice',
    initialState,
    reducers: {
        // 람다약식, 외부->내부는 {}
        joinRequest(state: IUserState, _payload){
            state.status = 'loading'
        },
        joinSuccess(state: IUserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload] // 저장 오버라이딩->오버로딩
        },
        joinFailed(state: IUserState, {payload}){
            state.status = 'failed'
            state.data = [...state.data, payload]
        },


        loginRequest(state: IUserState, _payload){
            state.status = 'loading'
        },
        loginSuccess(state: IUserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        loginFailed(state: IUserState, {payload}){
            state.status = 'failed'
            state.data = [...state.data, payload]
        }
    }
})

export const {joinRequest, joinSuccess, joinFailed,
     loginRequest, loginSuccess, loginFailed
    } = userSlice.actions
export default userSlice