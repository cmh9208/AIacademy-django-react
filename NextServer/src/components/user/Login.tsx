import { onProps } from "@/modules/types";

export default function Login({onChange, onSubmit}: onProps){

    return (
        <>
            <h1>로그인</h1>
            <form onSubmit={onSubmit}>
                <label htmlFor="user_email">이메일(ID):</label>
                <input type="text"  id="user_email" name="user_email" onChange={onChange} required minLength= {10} maxLength={20}/>
                <br/>
                <label htmlFor="password">Password:</label>
                <input type="text" id="password" name="password"  onChange={onChange} required />
                <br/>
                <button type="submit">Submit</button>
                
            </form> 
        </>
 );
}