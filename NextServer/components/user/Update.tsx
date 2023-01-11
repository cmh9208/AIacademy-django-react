import React, { useCallback, useState } from 'react';
import { useDispatch } from 'react-redux';
//import { modify } from 'features/user/reducer/userSlice'

import styled from 'styled-components'

export default function UpdateUser() {
    const dispatch = useDispatch()
    
  return (
    <Main>
         <h1>회원정보 수정</h1>
         <form action="/send-data-here" method="put" >

          <label htmlFor="user_email">User Email:</label>
          <div id="user_email" ></div>

          <label htmlFor="password">Password:</label>
          <input type="text" id="password" name="password" required />

          <label htmlFor="user_name">user_name:</label>
          <div id="user_name" ></div>

          <label htmlFor="phone">phone:</label>
          <input type="text" id="phone" name="phone" />

          <label htmlFor="birth">birth:</label>
          <div id="birth" ></div>

          <label htmlFor="address">address:</label>
          <input type="text" id="address" name="address" />

          <label htmlFor="job">job:</label>
          <input type="text" id="job" name="job" />

          <label htmlFor="user_interests">user_interests:</label>
          <input type="text" id="user_interests" name="user_interests" />

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