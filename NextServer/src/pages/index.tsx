import type { ReactElement } from 'react'
import Layout from '@/components/admin/Layout'
import Home from '@/components/Home'
import type { NextPageWithLayout } from '@/pages/_app'


const Page: NextPageWithLayout = () => {
  return <Home/>
}

Page.getLayout = function getLayout(page: ReactElement) {
  return (
    <Layout>
      {page}
    </Layout>
  )
}

export default Page