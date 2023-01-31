import React from 'react';
/**
type Props = {
    props: (e: React.FormEvent<HTMLFormElement>) => void
} */

export default function Logout({props}: any){
    return (
    <form onSubmit={props}>
        <button type="submit"> 로그아웃</button>
    </form>
)}