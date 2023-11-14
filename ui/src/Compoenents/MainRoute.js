import React from 'react'
import NavigationCMP from './NavigationCMP'
import { Outlet } from 'react-router-dom'

export default function MainRoute() {
  return (
    <React.Fragment>
        <NavigationCMP />
        <div className='mt-5 container'>
        <Outlet />
        </div>
    </React.Fragment>
  )
}
