import Head from "next/head"

type TitleProps = { title: string | string[] | undefined }

export function SEO({title}: TitleProps) {
    return (<Head>
        <title>{title}</title>
    </Head>)
}