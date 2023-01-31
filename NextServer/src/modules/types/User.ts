export interface User{
    userid? : string,
    email? : string,
    password? : string,
    cpassword?: string, 
    username? : string,
    phone? : string,
    birth? : string,
    address? : string,
    job? : string,
    interests? : string,
    token? : string,
    created? : string,
    modified? : string
}
export interface UserLoginInput{
    email: string,
    password: string
}
export interface UserUpdate{
    userid?: string,
    phone?: string,
    job?: string,
    interests?: string,
    modified?: string
}
export interface LoginUser{ 
    username?:string, password:string, email:string, userid?:string,
    phone?:string, birth?:string, 
    token?: any
}

export interface UserInfo{
    username:string, password:string, email:string,
    phone:string, birth:string,
    token: any
}

export interface UserInfoState{
    data: UserInfo[]
    isloggined: boolean
}

export interface UserState{
    data: User[]
    status: 'idle' | 'loading' | 'failed'
    token?: null,
    isLoggined: boolean,
    error : null;
    loginedUser: null,
    check: boolean
}