import { all, fork } from "redux-saga/effects"
import{
    watchJoin
}from "./userSagas"

export default function* rootSaga(){
    yield all([
        fork(watchJoin)
    ])
}