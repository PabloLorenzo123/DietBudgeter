import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";
import api from "../api";
import AuthForm from "./components/AuthForm";

const Login = ({setAuthorized}) => {
    return (
        <AuthForm
            action={"login"}
            title={"Welcome Back"}
            btnText={'LOG IN'}
            setAuthorized={setAuthorized}
        />
    )
}

export default Login
