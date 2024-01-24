import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default function handleProfileSignup(firstName, lastName, fileName){
    Promise.allSettled([signUpUser(firstName, lastName), fileName]).then(console.log).catch(console.log)
}