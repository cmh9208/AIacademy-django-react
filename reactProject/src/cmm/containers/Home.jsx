import { Route, Routes } from "react-router-dom"
import {Navigation2, Counter, Footer} from "cmm"
import {Schedule} from "cop"
import {LoginForm, SignUp} from "uat"
import image from '../../images/fashion.png'


import React from 'react'
import { Stroke } from "blog"


//Three.js
// import { Canvas } from '@react-three/fiber'
// import { OrbitControls } from '@react-three/drei'
import { Fashion } from "fashion"
import { Number } from "number"
import { Webcrawler } from "webcrawler"
import { Samsung } from "nlp"
import { NaverMovie } from "naver_movie"
import { UsersList } from "users"
import { NaverMovieReview } from "imdb"
import { Iris } from "iris"



const Home = () => {
    const imageSize = {width: 700, height: 500}
    return (<>
    <table style={{ width: "1200px", height: "550px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr columns="3" >
                <td style={{ width: "100%", height: "150px", border: "1px solid black"}}>
                    <Navigation2/>
                </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%", height: "80%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Routes>
                <Route path="/counter" element={<Counter/>}></Route>
                <Route path="/counter" element={<Counter/>}></Route>
                <Route path="/todos" element={<Schedule/>}></Route>
                <Route path="/login" element={<LoginForm/>}></Route>
                <Route path="/signup" element={<SignUp/>}></Route>
                <Route path="/stroke" element={<Stroke/>}></Route>
                <Route path="/iris" element={<Iris/>}></Route>
                <Route path="/fashion" element={<Fashion/>}></Route>
                <Route path="/number" element={<Number/>}></Route>
                <Route path="/webcrawler" element={<Webcrawler/>}></Route>
                <Route path="/samsung" element={<Samsung/>}></Route>
                <Route path="/naver" element={<NaverMovie/>}></Route>
                <Route path="/users" element={<UsersList/>}></Route>
                <Route path="/imdb" element={<NaverMovieReview/>}></Route>
            </Routes>
            
            </td>
            
        </tr>
        <tr>
            <td>
                <img src={image} style={imageSize}/>
                {/* <Contain style={{ width: "100vw", height: "50vh", background: "black"}}>
                <Canvas >
                    <Suspense fallback={null}>
                        <directionalLight intensity={1} />
                        <ambientLight intensity={1.2} />
                        <spotLight intensity={2} angle={2} penumbra={1} position={[10, 15, 10]} castShadow />
                        <Model />
                        <OrbitControls enablePan={true} enableZoom={true} enableRotate={true} />
                    </Suspense>
                </Canvas>
                </Contain> */}
            </td>
        </tr>
        <tr style={{ width: "100%", height: "20%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
                <Footer/>
            </td>
        </tr>
        </tbody>
    </table>
    </>)
}
export default Home

// function Model({ ...props }) {
//     const group = useRef()
//     const { nodes, materials } = useGLTF('/scene.gltf')
//     return (
//       <group ref={group} {...props} dispose={null} scale={0.03}>
//         <group rotation={[-Math.PI / 2, 0, 0]}>
//           <mesh geometry={nodes.Object_2.geometry} material={materials['9smg1']} />
//           <mesh geometry={nodes.Object_3.geometry} material={materials['9smg2']} />
//         </group>
//       </group>
//     )
//   }
  
// const Contain = styled.div`
//     width:100%;
//     height:100%;
//     margin:0 auto;
//     background:#eee;
// `