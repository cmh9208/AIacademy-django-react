import '../styles/UserList.css'
import {useState, useEffect} from 'react'
import axios from 'axios'

export default function UserList(){
    const [list, setList] = useState([])
    useEffect(()=>{
        axios
        .get('http://localhost:8000/security/users/list')
        .then(res => {setList(res.data)})
        .catch(err => {console.log(err)})
    }, [])
   
    return <>
        
    </>
}


