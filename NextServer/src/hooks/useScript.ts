import { AppDispatch, AppState } from '@/modules/store';
import {useEffect} from 'react';
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux'

export const useAppDispatch : () => AppDispatch = useDispatch
export const useAppSelector: TypedUseSelectorHook<AppState> = useSelector;

export const useScript = (url: string, onload: () => void) => {
    useEffect(() => {
      const script = document.createElement('script');
  
      script.src = url;
      script.onload = onload;
  
      document.head.appendChild(script);
      
      return () => {
        document.head.removeChild(script);
      };
    }, [url, onload]);
  };