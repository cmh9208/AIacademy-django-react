export default function FindEmail(){

    return (
        <>
            <h1>비밀번호 찾기</h1>
            <form action="/send-data-here">
                <label htmlFor="user_email">User Email:</label>
                <input type="text"  id="user_email" name="user_email" required minLength= {10} maxLength={20}/>
                <button type="submit">Submit</button>
            </form> 
        </>
            
        
 );
}
