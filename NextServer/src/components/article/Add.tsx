import { useDispatch } from "react-redux"
import {  writeRequest } from "@/modules/slices"
import { SubmitHandler, useForm} from "react-hook-form"
import { Article } from "@/modules/types";
import { useRef } from "react"

export default function Add() {
    const dispatch = useDispatch()
    const { register, handleSubmit, formState: { errors }  } = useForm<Article>()
    const onSubmit: SubmitHandler<Article> = data => {
      alert(`1 - 리액트에 입력된 글 정보 : ${JSON.stringify(data)}`)
      dispatch(writeRequest(data))
    };

   
   return(<>
    <form onSubmit={handleSubmit(onSubmit)} method="post">
    <label htmlFor="title">타이틀 :</label>
          <input 
          {...register("title", { 
            
            maxLength: {
                value: 100,
                message: "100자 이하로 입력해주세요"
            }
        })}
          type="text" id="title" name="title" /> <br/>

    <label htmlFor="content">내용 :</label>
              <input 
              {...register("content", { 
                
                maxLength: {
                    value: 1000,
                    message: "1000자 이하로 입력해주세요"
                }
            })}
              type="text" id="content" name="content" /> <br/>
  
  <label htmlFor="userid">아아디 :</label>
              <input 
              {...register("userid", { 
                
                maxLength: {
                    value: 30,
                    message: "30자 이하로 입력해주세요"
                }
            })}
              type="text" id="userid" name="userid" /> <br/>
  
      <button type="submit" >전송</button>


    </form>
    
    </>)
}

