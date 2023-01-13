import { ReactNode } from "react";

export interface onProps{
    onSubmit: (e : React.FormEvent<HTMLFormElement>) => void
    onChange: (e : React.ChangeEvent<HTMLInputElement> ) => void
}

export interface Layout {
    children?: ReactNode
}

export * from './User';
export * from './Article';