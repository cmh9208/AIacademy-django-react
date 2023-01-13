import { all, fork } from "redux-saga/effects"
import{
    watchJoin, watchLogin
} from "./userSaga"

export default function* rootSaga(){
    yield all([ fork(watchJoin), fork(watchLogin)])
}