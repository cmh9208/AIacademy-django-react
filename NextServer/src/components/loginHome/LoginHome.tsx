import Link from "next/link"

type Props = {
    email: string | undefined
}

export default function LoginHome({email} : Props){
    return (<>
        <h5>{email}님 반갑습니다.</h5>
        </>)
        
}