import React from 'react'

import { Helmet } from 'react-helmet'

import Navbar4 from '../components/navbar4'
import Hero3 from '../components/hero3'
import Logos1 from '../components/logos1'
import Gallery1 from '../components/gallery1'
import Features17 from '../components/features17'
import Features18 from '../components/features18'
import Features171 from '../components/features171'
import CTA1 from '../components/cta1'
import FAQ1 from '../components/faq1'
import Contact4 from '../components/contact4'
import Footer15 from '../components/footer15'
import './home.css'

const Home = (props) => {
  return (
    <div className="home-container">
      <Helmet>
        <title>Pesky Flamboyant Newt</title>
        <meta property="og:title" content="Pesky Flamboyant Newt" />
      </Helmet>
      <div className="home-navbar1">
        <Navbar4></Navbar4>
      </div>
      <div className="home-hero2">
        <Hero3
          image1Src="https://img.freepik.com/free-photo/man-neon-suit-sits-chair-with-neon-sign-that-says-word-it_188544-27011.jpg"
          heading1="Hello, I'm Anmol Siwa (Justin)"
        ></Hero3>
      </div>
      <div className="home-logos3">
        <Logos1></Logos1>
      </div>
      <div className="home-gallery4">
        <Gallery1></Gallery1>
      </div>
      <div className="home-features5">
        <Features17></Features17>
      </div>
      <div className="home-features6">
        <Features18></Features18>
      </div>
      <div className="home-features7">
        <Features171></Features171>
      </div>
      <div className="home-cta8">
        <CTA1></CTA1>
      </div>
      <div className="home-faq9">
        <FAQ1></FAQ1>
      </div>
      <div className="home-contact10">
        <Contact4></Contact4>
      </div>
      <div className="home-footer11">
        <Footer15></Footer15>
      </div>
    </div>
  )
}

export default Home
