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