import { SubmitHandler, useForm} from "react-hook-form"
import { User } from "@/modules/types"
import { useRef } from "react"
import { useDispatch } from "react-redux"
import { joinRequest } from "@/modules/slices"

export default function Join() { 
    const dispatch = useDispatch()
    const { register, handleSubmit, watch, formState: { errors }  } = useForm<User>()
    const onSubmit: SubmitHandler<User> = data => {
      alert(`1 - 리액트에 입력된 회원정보 : ${JSON.stringify(data)}`)
      dispatch(joinRequest(data))
    };
    const passwordRef = useRef<string | null | undefined>(null)
    passwordRef.current = watch("password")
    return (<>
        <h2>회원가입</h2>
        <form onSubmit={handleSubmit(onSubmit)}>

          <label htmlFor="user_email">이메일(ID):</label>
          <input 
            {...register("user_email", { 
              required: true,
              maxLength: 30,
              pattern: {
                  value: /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/,
                  message: "이메일 형식에 맞게 입력해주세요"
              }
          })}
            type="text"  id="user_email" name="user_email" 
            placeholder="name@example.com"
            required minLength= {10} maxLength={20}/> <br/>
            
            {errors.user_email && <p>{errors.user_email.message}</p>}
            <br/>
          <label htmlFor="password">비밀번호:</label>
          <input 
            {...register("password", { 
              required: true, 
              minLength: {
                  value: 4,
                  message: "4자 이상 입력해주세요"
              },
              pattern: {
                  value: /^(?=.*\d)(?=.*[a-zA-ZS]).{4,}/,
                  message: "영문, 숫자를 혼용하여 입력해주세요"
              }
            })}
            type="password" 
            placeholder="비밀번호(영문, 숫자 8자리 이상)"
            id="password" name="password" required /> <br/>
          {errors.password && <p>{errors.password.message}</p>}
          <input
                        {...register("cpassword", { 
                            required: true,
                            validate: (value) => value === passwordRef.current,
                         })}
                        type="password"
                        placeholder="비밀번호 재확인"
                        id="cpassword"
                        name="cpassword"
                        className="block w-full px-4 py-3 text-sm border rounded-lg outline-none"/>
                    {errors.cpassword && <p>비밀번호가 일치하지 않습니다</p>}
                    <br/>
                    <br/>
          <label htmlFor="user_name">이름(실명):</label>
          <input
          {...register("user_name", { 
            required: true, 
            maxLength: {
                value: 20,
                message: "20자 이하로 입력해주세요"
            }
        })}
          
          type="text" id="user_name" name="user_name" 
          placeholder="사용자 이름"
          required /> 
        {errors.user_name && <p>{errors.user_name.message}</p>}<br/>
        <br/>
          <label htmlFor="phone">전화번호:</label>
          <input type="text" id="phone" name="phone" required /> <br/>
          <br/>
          <label htmlFor="birth">생년월일(20001201):</label> 
          <input 
          {...register("birth", { 
            required: true, 
            maxLength: {
                value: 8,
                message: "생년월일 8자리까지 입력해주세요"
            },
            minLength:{
                value: 8,
                message:"생년월일 8자리까지 입력해주세요"  
            },
            pattern: {
                value: /^[0-9]+$/,
                message:"숫자만 입력해주세요"
            }
        })}
          
          type="text" id="birth" name="birth" 
          placeholder="생년월일 8자리(ex: 19991212)"
          /> 
          {errors.birth && <p>{errors.birth.message}</p>}
          <br/>
          <br/>

          <label htmlFor="address">주소:</label>
          <input type="text" id="address" name="address" /> <br/>
          <br/>

          <label htmlFor="job">직업:</label>
          <input type="text" id="job" name="job" /> <br/>
          <br/>

          <label htmlFor="user_interests">관심사항 :</label>
          <input type="text" id="user_interests" name="user_interests" /> <br/>
          <br/>
          <input type="checkbox" className="custom-control-input" id="aggrement" required />
                    <label className="custom-control-label" htmlFor="aggrement">개인정보 수집 및 이용에 동의합니다.</label>
          <br/>
          <br/>
          <button type="submit">Submit</button>
          </form> 
        </>)

    }