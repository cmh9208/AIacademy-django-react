import React from 'react';

export default function Logout(){
    return <button
        onClick = { e => {
            e.preventDefault()
            e.stopPropagation()
            localStorage.clear()
            
        }}> 로그아웃
    </button>}

