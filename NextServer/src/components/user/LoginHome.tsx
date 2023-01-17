type Props = { email: string | undefined}

interface LoginProps{
    handleChange : (e: React.ChangeEvent<HTMLInputElement>) => void
    handleSubmit : (e: React.ChangeEvent<HTMLFormElement>) => void
}

export default function LoginHome({email}: Props){
    return (
        <div>
            <h2>{email} 로그인 중 ..</h2>
        </div>
    )
}