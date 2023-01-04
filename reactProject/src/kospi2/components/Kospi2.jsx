import naverMovieReviewService from "../api"
import { useState } from "react"

const Korean2 = ()=> {
    const [inputs, setInputs] = useState({})
    const [positive, setPositive] = useState('')
    const [positive1, setPositive1] = useState('')
    const [positive2, setPositive2] = useState('')
    const [positive3, setPositive3] = useState('')
    const [positive4, setPositive4] = useState('')
    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }

    const onClick = e =>{
        e.preventDefault()
        naverMovieReviewService.classifyPositiveAboutReview(inputs).then(res => {
            const json = JSON.parse(res)
            setPositive(json["result"])
            setPositive1(json["result1"])
            setPositive2(json["result2"])
            setPositive3(json["result3"])
            setPositive4(json["result4"])
            alert(`결과 알림창: ${JSON.stringify(json["result"])}
                 ${JSON.stringify(json["result1"])}
                 ${JSON.stringify(json["result2"])}
                 ${JSON.stringify(json["result3"])}
                 ${JSON.stringify(json["result4"])}`)
            
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (<>
    <h5>삼성 주가 예측</h5>
    <form method="post">확인할 날짜 : 
    <input type="text" className="box" placeholder="입력" name="inputs" onChange={onChange}
    />
    <button type="submit" onClick={onClick}>확인된 값</button></form>
    <table>
        <thead>
            <tr>
                <th>입력 날짜 이후 4일까지</th>
            </tr>
        </thead>
        <tbody>
        {positive && 
            <tr ><td>{positive} </td></tr>
        }
        {positive1 && 
            <tr ><td>{positive1} </td></tr>
        }
        {positive1 && 
            <tr ><td>{positive2} </td></tr>
        }
        {positive1 && 
            <tr ><td>{positive3} </td></tr>
        }
        {positive1 && 
            <tr ><td>{positive4} </td></tr>
        }  
        </tbody>
    </table>     
    </>)
}
export default Korean2