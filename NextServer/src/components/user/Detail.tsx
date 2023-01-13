import { useState } from "react"


export default function UserDetail() {

    return (<>
        <h2>회원정보</h2>
        <div>

          <label htmlFor="user_email">User Email:</label>
          <div id="user_email" ></div>

          <label htmlFor="password">Password:</label>
          <div id="password" ></div>

          <label htmlFor="user_name">user_name:</label>
          <div id="user_name" ></div>

          <label htmlFor="phone">phone:</label>
          <div id="phone" ></div>

          <label htmlFor="birth">birth:</label>
          <div id="birth" ></div>

          <label htmlFor="address">address:</label>
          <div id="address" ></div>

          <label htmlFor="job">job:</label>
          <div id="job" ></div>

          <label htmlFor="address">address:</label>
          <div id="address" ></div>

          <label htmlFor="user_interests">user_interests:</label>
          <div id="user_interests" ></div>


          <button>수정하기</button>
          </div> 
        </>)
}
