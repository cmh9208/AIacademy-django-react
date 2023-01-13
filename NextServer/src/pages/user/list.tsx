import { NextPage } from "next"
const UserListPage: NextPage =  function(){
    
    return <>
        <table className='user-list'>
            <thead>
                <tr>
                <th>ID</th><th>이메일</th><th>이름</th><th>전화번호</th>
                <th>생년월일</th><th>주소</th><th>직업</th><th>관심사항</th>
                </tr>
            </thead>
            <tbody>
            
            </tbody>
        </table>
    </>
}
export default UserListPage


