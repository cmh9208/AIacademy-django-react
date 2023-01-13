export const currentTime = function(){
    let today = new Date();   
    return `${today.getHours()}시 ${today.getMinutes()}분 ${today.getSeconds()}초`
}