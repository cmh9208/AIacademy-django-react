export default function Join() { 
  return (<>
      <h2>회원가입</h2>
      <form action="/send-data-here" method="post" >

        <label htmlFor="user_email">User Email:</label>
        <input type="text"  id="user_email" name="user_email" required minLength= {10} maxLength={20}/> <br/>

        <label htmlFor="password">Password:</label>
        <input type="text" id="password" name="password" required /> <br/>

        <label htmlFor="user_name">user_name:</label>
        <input type="text" id="user_name" name="user_name" required /> <br/>

        <label htmlFor="phone">phone:</label>
        <input type="text" id="phone" name="phone" required /> <br/>

        <label htmlFor="birth">Birth:</label> 
        <input type="text" id="birth" name="birth" /> <br/>

        <label htmlFor="address">address:</label>
        <input type="text" id="address" name="address" /> <br/>

        <label htmlFor="job">job:</label>
        <input type="text" id="job" name="job" /> <br/>

        <label htmlFor="lastuser_interests">user_interests:</label>
        <input type="text" id="user_interests" name="user_interests" /> <br/>


        <button type="submit">Submit</button>
        </form> 
      </>)

  }