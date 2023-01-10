import React from 'react';
import Header from './Header';
import Footer from './Footer';
export default function Layout(props: any){
    return (
      <div>
        <Header/>
        <main>
        {props.children}
        </main>
        <Footer />
      </div>
    )
  }
  
