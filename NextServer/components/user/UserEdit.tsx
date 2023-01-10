import React, { useCallback, useState } from 'react';
import { useDispatch } from 'react-redux';
//import { modify } from 'features/user/reducer/userSlice'

import styled from 'styled-components'

export default function UserEdit() {
    const dispatch = useDispatch()
    
  return (
    <Main>
         <h1>회원정보 수정</h1>
    </Main>
   
  );
}
const Main = styled.div`
width: 500px;
margin: 0 auto;
text-decoration:none
text-align: center;
`