import * as React from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import RestoreIcon from '@mui/icons-material/Restore';
import FavoriteIcon from '@mui/icons-material/Favorite';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import { Link } from "react-router-dom"

const Navigation2 = () => {
  const [value, setValue] = React.useState(0);

  return (
    <Box sx={{ width: 500 }}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      >
        <Link to="/home" style={{width:50, margin:10}}>Home</Link>
        <Link to="/counter" style={{width:50, margin:10}}>Counter</Link>
        <Link to="/todos" style={{width:50, margin:10}}>Todos</Link>
        <Link to="/stroke" style={{width:30, margin:10}}>뇌졸증</Link>
        <Link to="/iris" style={{width:30, margin:10}}>아이리스</Link>
        <Link to="/fashion" style={{width:30, margin:10}}>패션</Link>
        <Link to="/number" style={{width:30, margin:10}}>넘버</Link>
        <Link to="/webcrawler" style={{width:30, margin:10}}>크롤러</Link>
        <Link to="/samsung" style={{width:30, margin:10}}>삼성</Link>
        <Link to="/naver" style={{width:30, margin:10}}>네이버</Link>
        <Link to="/imdb" style={{width:30, margin:10}}>리뷰 분석</Link>
        <Link to="/korean" style={{width:30, margin:10}}>언어감지</Link>
        <Link to="/aitrader" style={{width:30, margin:10}}>삼성주식</Link>

        
        <Link to="/login" style={{width:50, margin:10}}>로그인</Link>
        <Link to="/signup" style={{width:50, margin:10}}>회원가입</Link>
        <Link to="/list" style={{width:30, margin:10}}>유저목록</Link>
      </BottomNavigation>
    </Box>
  );
}

export default Navigation2