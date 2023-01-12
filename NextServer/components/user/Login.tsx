import {userLogin} from '@/pages/api';



export default function Login(){
    return (
        <><button
        onClick = { e => {
            e.preventDefault()
            userLogin()
            alert(`눌러짐`)
        }}> FastAPI로 보내기 테스트
         </button>
         
            <h1>로그인</h1>
            <form action="/send-data-here" method="post" >
                <label htmlFor="user_email">User Email:</label>
                <input type="text"  id="user_email" name="user_email" required minLength= {10} maxLength={20}/>
                <br/>
                <label htmlFor="password">Password:</label>
                <input type="text" id="password" name="password" required />
                <br/>
                <button type="submit">Submit</button>
            </form> 
        </>
            
        
 );
}

