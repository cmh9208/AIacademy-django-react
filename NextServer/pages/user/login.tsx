import { NextPage } from "next"
import { Login,  GoogleLogin} from "@/components/user"
import React from 'react';



const LoginPage: NextPage = function(){

    return (
        <>
           <Login/>
           <br/>
           <br/>
           <GoogleLogin/>
        </>
            
        
 );
}
export default LoginPage


