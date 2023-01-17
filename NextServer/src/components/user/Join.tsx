import { SubmitHandler, useForm} from "react-hook-form"
import { User } from "@/modules/types"
import { useRef } from "react"
import { useDispatch } from "react-redux"
import { joinRequest } from "@/modules/slices"
import styled from 'styled-components';

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
        
        <form onSubmit={handleSubmit(onSubmit)}>
          <Sheet >
            <thead>
              <Row>
                <Cell colSpan={2}><h6>회원가입</h6></Cell>
              </Row>
            </thead>
            <tbody>
              <Row>
                <Cell>
                <label htmlFor="email">이메일(ID)</label></Cell>
                <Cell><Input 
            {...register("email", { 
              required: true,
              maxLength: 30,
              pattern: {
                  value: /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/,
                  message: "이메일 형식에 맞게 입력해주세요"
              }
          })}
            type="text"  id="email" name="email" 
            placeholder="name@example.com"
            required minLength= {10} maxLength={20}/> <br/>
            
            {errors.email && <p>{errors.email.message}</p>} </Cell></Row>
            <Row><Cell>
          <label htmlFor="password">비밀번호</label></Cell>
          <Cell><Input 
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
            id="password" name="password" required /> 
          {errors.password && <p>{errors.password.message}</p>}
          
          <Input
                        {...register("cpassword", { 
                            required: true,
                            validate: (value) => value === passwordRef.current,
                         })}
                        type="password"
                        placeholder="비밀번호 재확인"
                        id="cpassword"
                        name="cpassword"
                        />
                    {errors.cpassword && <p>비밀번호가 일치하지 않습니다</p>}
                </Cell>
              </Row>
             
              <Row>
                <Cell>
                <label htmlFor="username">이름(실명)</label></Cell><Cell>
          <Input
          {...register("username", { 
            required: true, 
            maxLength: {
                value: 20,
                message: "20자 이하로 입력해주세요"
            }
        })}
          
          type="text" id="username" name="username" 
          placeholder="사용자 이름"
          required /> 
        {errors.username && <p>{errors.username.message}</p>}
                </Cell>
              </Row>
              <Row>
                <Cell>
                <label htmlFor="phone">전화번호</label></Cell>
                <Cell><Input type="text" id="phone" name="phone" /> 

                </Cell>
              </Row>
              <Row>
                <Cell>
                <label htmlFor="birth">생년월일</label> </Cell>
                <Cell><Input 
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
                </Cell>
              </Row>
              <Row>
                <Cell><label htmlFor="address">주소</label></Cell>
                <Cell><Input type="text" id="address" name="address" /> </Cell>
              </Row>
              <Row>
                <Cell>
                <label htmlFor="job">직업</label></Cell>
                <Cell><Input type="text" id="job" name="job" /> 
                </Cell>
              </Row>
              <Row>
                <Cell>
                <label htmlFor="interests">관심사항</label></Cell>
                <Cell><Input type="text" id="interests" name="interests" /> 
                </Cell>
              </Row>
              <Row>
                <Cell>
                <Input type="checkbox" className="custom-control-input" id="aggrement" required /></Cell>
                <Cell><label className="custom-control-label" htmlFor="aggrement">개인정보 수집 및 이용에 동의합니다.</label>
                </Cell>
              </Row>
              <Row>
                <Cell colSpan={2}><button type="submit" >전송</button></Cell>
              </Row>
              
            </tbody>
          </Sheet>

          
          </form> 
        </>)

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