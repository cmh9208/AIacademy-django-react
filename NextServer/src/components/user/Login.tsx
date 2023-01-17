import { onProps } from "@/modules/types";
import styled from 'styled-components';
import React, { useRef } from 'react'
type Props = {
    onChange : (e : React.FormEvent<HTMLTextAreaElement | HTMLInputElement>) => void
    onSubmit : (e : React.FormEvent<HTMLFormElement>) => void
}

export default function Login({onChange, onSubmit}: Props){

    const emailRef = useRef<HTMLInputElement>(null)
    const passwordRef = useRef<HTMLInputElement>(null)
    return (
        <>
            <form onSubmit={onSubmit}>
                <Sheet>
                    <thead>
                        <Row>
                            <Cell colSpan={2}><h6>로그인</h6></Cell>
                        </Row>
                    </thead>
                    <tbody>
                        <Row>
                            <Cell><label htmlFor="email">이메일(ID)</label></Cell>
                            <Cell><Input type="text"  id="email" name="email" ref = {emailRef} onChange={onChange}  required minLength= {10} maxLength={20}/></Cell>
                        </Row>
                        <Row>
                            <Cell><label htmlFor="password">비밀번호</label></Cell>
                            <Cell><Input type="text" id="password" name="password" ref = {passwordRef} onChange={onChange}  required /></Cell>
                        </Row>
                        <Row>
                            <Cell colSpan={2}><button type="submit">전송</button></Cell>
                        </Row>
                    </tbody>
                </Sheet>
            </form> 
        </>
 );
}


const Sheet = styled.table`
border: 1px solid black
width: 70%
`
const Row = styled.tr`
border: 1px solid black
`
const Cell = styled.td`
border: 1px solid black,
`
const Input = styled.input`
width: 100%
`