import '../styles/UserList.css'
export default function ListForm({list:[]}){

    return (<><h2>User List</h2>
        <table className='user-list'>
            <thead>
                <tr>
                <th>ID</th><th>이메일</th><th>비번</th><th>이름</th><th>전화번호</th>
                <th>생년월일</th><th>주소</th><th>직업</th><th>관심사항</th>
                </tr>
            </thead>
            <tbody>
            
            </tbody>
        </table></> )
}


