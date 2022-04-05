import React from 'react'
import './SignUp.css'
import {Route, Link, Routes, Navigate} from "react-router-dom"

function SignUp() {
  return (
      <div className='sign_up_page'>
        <div className='sign_up_container'>
          <h1 className='sign_up_header'>Sign Up</h1>
          <hr></hr>
          <h2 className='welcome'>Welcome to Pawbnb</h2>

          <form className='sign_up_form'>
            <input className='sign_up_email_input' type="email" name="email" placeholder="Email"/>
            <input className='sign_up_ps_input' type="password" name="password" placeholder="Password"/>
            <input className='sign_up_submit' type="submit" value="Submit"/>
          </form>
        </div>

        <footer>
          <p>© 2022 Pawbnb Inc.</p>
        </footer>
      </div>
  )
}

export default SignUp