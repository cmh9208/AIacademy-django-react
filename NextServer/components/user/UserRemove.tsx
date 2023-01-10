import React, { useCallback, useState } from 'react';

import { useDispatch } from 'react-redux';

import styled from 'styled-components'
export default function UserRemove() {
  const [pwd, setPwd] = useState('')


  const dispatch = useDispatch()
  return (
    <Main>
      <h1>회원탈퇴</h1>
      
    <ul>
        <li>
              <label>
                    <span>사용자아이디 : </span>
                </label>
            </li>
        <li><label htmlFor="pw">비밀번호 확인</label>
        <input type="password" id="password" name="password" onChange={e => {setPwd(e.target.value)}}/></li>
        <li><input type="submit" value="탈퇴요청" /></li>
        <li><input type="button" value="탈퇴취소"/></li>
    </ul>


</Main>
  );
}

const Main = styled.div`
width: 500px;
margin: 0 auto;
text-decoration:none
text-align: center;
`