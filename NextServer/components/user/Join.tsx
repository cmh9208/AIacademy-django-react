export default function Join() { 
  return (<>
      <h2>회원가입</h2>
      <form method="post" >

        <label htmlFor="userEmail">이메일(ID):</label>
        <input type="text"  id="userEmail" name="userEmail" required minLength= {10} maxLength={20}/> <br/>

        <label htmlFor="password">비밀번호:</label>
        <input type="text" id="password" name="password" required /> <br/>

        <label htmlFor="userName">이름(실명):</label>
        <input type="text" id="userName" name="userName" required /> <br/>

        <label htmlFor="phone">전화번호:</label>
        <input type="text" id="phone" name="phone" required /> <br/>

        <label htmlFor="birth">생년월일(20001201):</label> 
        <input type="text" id="birth" name="birth" /> <br/>

        <label htmlFor="address">주소:</label>
        <input type="text" id="address" name="address" /> <br/>

        <label htmlFor="job">직업:</label>
        <input type="text" id="job" name="job" /> <br/>

        <label htmlFor="lastuserInterests">관심사항 :</label>
        <input type="text" id="userInterests" name="userInterests" /> <br/>


        <button type="submit">Submit</button>
        </form> 
      </>)

  }