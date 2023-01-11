import React, { useCallback, useState } from 'react';

import { useDispatch } from 'react-redux';

import styled from 'styled-components'
export default function RemoveUser() {
  const [pwd, setPwd] = useState('')


  const dispatch = useDispatch()
  return (
    <Main>
      <h1>회원탈퇴</h1>
            <form action="/send-data-here">
                <label htmlFor="user_email">비밀번호 확인:</label>
                <input type="text"  id="password" name="password" required/>
                <button type="submit">Submit</button>
            </form> 
</Main>
  );
}

const Main = styled.div`
width: 500px;
margin: 0 auto;
text-decoration:none
text-align: center;
`