import React from "react";
import "./SalesPage.css";

import {Container} from '@mui/material';

import SalesList from "./SalesList";


const SalesPage = (props) => {

    const { sales } = props;

    return(
        <React.Fragment>
            <SalesList sales={sales} />
        </React.Fragment>
    )
};


export default SalesPage;