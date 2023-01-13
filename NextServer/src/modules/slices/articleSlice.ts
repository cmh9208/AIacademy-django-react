import { createSlice } from "@reduxjs/toolkit"
import { Article } from '@/modules/types'

type ArticleState = {
    data: Article[]
    status: 'idle' | 'loading' | 'failed'
    isLoggined: boolean
    error: any
}
const initialState: ArticleState = {
    data: [],
    status: 'idle',
    isLoggined: false,
    error: null
}

const articleSlice = createSlice({
    name: 'articleSlice',
    initialState,
    reducers: {
        writeRequest(state: ArticleState, _payload){
            state.status = 'loading'
        },
        writeSuccess(state: ArticleState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        writeFailure(state: ArticleState, {payload}){
            state.status = 'failed'
            state.data = [...state.data, payload]
        }
    }
})

const {reducer, actions} = articleSlice
export const {writeRequest, writeSuccess, writeFailure
} = articleSlice.actions
export const articleAction = actions
export default reducer