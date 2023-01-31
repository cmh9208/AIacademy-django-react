import axios from "axios";
import next from "next";
import {useState, useEffect} from "react"
import Pagination from "./admin/Pagination";



export default function Home(){

   const [list, setList] = useState([])
   const [rowCnt, setRowCnt] = useState(0)
   const [requestPage, setRequestPage] = useState(0)
   const [startRowPerPage, setStartRowPerPage] = useState(0)
   const [endRowPerPage, setEndRowPerPage] = useState(0)
   const [startPagePerBlock, setStartPagePerBlock] = useState(0)
   const [endPagePerBlock, setEndPagePerBlock] = useState(0)
   const [rows, setRows] = useState<number[]>([])
   const [pages, setPages] = useState<number[]>([])
   const [prevArrow, setPrevArrow] = useState(false)
   const [nextArrow, setNextArrow] = useState(false)

    useEffect(()=>{
        axios
        .get('http://localhost:8000/users/page/1')
        .then(res => {
            setRowCnt(Number(res.data.pager.row_cnt))
            setStartRowPerPage(Number(res.data.pager.start_row_per_page))
            setEndRowPerPage(Number(res.data.pager.end_row_per_page))
            setStartPagePerBlock(Number(res.data.pager.start_page_per_block))
            setEndPagePerBlock(Number(res.data.pager.end_page_per_block))
            setPrevArrow(res.data.pager.prev_arrow)
            setNextArrow(res.data.pager.next_arrow)
            setRequestPage(Number(res.data.pager.request_page))
            alert(` 사용자가 요청한 페이지 번호: ${requestPage}`)
            console.log(` 사용자가 요청한 페이지 번호: ${requestPage}`)
            console.log(` 페이지 시작 행번호: ${startRowPerPage}`)
            console.log(` 페이지 마지막 행번호: ${endRowPerPage}`)
            console.log(` 블록 시작 페이지번호: ${startPagePerBlock}`)
            console.log(` 블록 마지막 페이지번호: ${endPagePerBlock}`)
            console.log(` 이전 보이는지 여부 체크 : ${prevArrow}`)
            console.log(` 이후 보이는지 여부 체크: ${nextArrow}`)
            setList(res.data.users.items)
            console.log(" ### 페이지 내용 표시 ### ")
            let rows:number[] = []
            let pages:number[] = []
            for(let i =startRowPerPage; i <= endRowPerPage; i++){
                console.log(`page index : ${i}`)
                rows.push(i)
            }
            setRows(rows)
            console.log(" ### 블록 내용 표시 ### ")
            for(let i =startPagePerBlock; i <= endPagePerBlock; i++){
              console.log(`block index : ${i}`)
              pages.push(i)
           }
           setPages(pages)
           
          
        })
        .catch(err => {console.log(err)})
    }, [])

  return (
    <>
    <h2>회원목록 </h2>
    <h6>회원수: {rowCnt}</h6>
    <h6></h6>
    <h6></h6>
    <h6></h6>
        <table className='user-list'>
            <thead>
                <tr>
                <th>ID</th><th>이메일</th><th>비번</th><th>이름</th><th>전화번호</th>
                <th>생년월일</th><th>주소</th><th>직업</th><th>관심사항</th>
                </tr>
            </thead>
            <tbody>
            <div>  { prevArrow && <span> 이전 </span>}</div>
            {list && list.map(({userid, email, username, phone, birth, address, job, interests})=>(
                <tr key={userid}>
                    <td>{userid}</td><td>{email}</td><td>{username}</td>
                    <td>{phone}</td><td>{birth}</td><td>{address}</td>
                    <td>{job}</td><td>{interests}</td>
                </tr>
            ))}
           <div>  
            { nextArrow && <span> 이후 </span>}</div>
            </tbody>
        </table>
        <div>
          {pages && pages.map((v, i) => (<span style={{"border": "1px solid black"}}  >{v+1}</span>))}
        </div>
        <div className="page-container">
    </div>
    </>
    
  );
}