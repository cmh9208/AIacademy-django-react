type Props = { email: string | undefined}
export default function LoginHome({email}: Props){
    return (
        <div>
            <h2>{email} 로그인 중 ..</h2>
        </div>
    )
}