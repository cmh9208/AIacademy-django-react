import React from 'react';
import styled from 'styled-components'
export default function Header(){
    return (
      <><header>
        {/* <Navigation/><br/> 
        <HR/>
        {localStorage.length > 0 ?
        <div>
            <Span>{JSON.parse(window.localStorage.getItem('sessionUser')).name}님 접속중 
            <Logout/></Span> 
        </div>
        : <>
        <Span><button onClick = {e => window.location.href = `/users/add`}>회원가입</button>
        <button onClick = {e => window.location.href = `/users/login`}>로그인</button></Span>
        </>}*/}
        
      </header>
      </>
    )
  }
const Span = styled.span`
    color: red;
    float: right;
    padding-right: 100px
`
const HR = styled.hr`
  border: 1px solid black;
  text-align: center;
`
